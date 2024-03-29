import uuid
import datetime as _dt
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import List, Optional
from ninja_extra import NinjaExtraAPI, api_controller, route
from api.models import Volunteer, Event, FormResponse
from api.schemas import (
    EventSchemaCreate,
    EventSchemaUpdate,
    FormResponseSchema,
    TimeseriesUnit,
    Success,
    UniqueVolunteers,
    VolunteerContributionsSchema,
    VolunteerSchema,
    EventSchemaWithoutVolunteers,
    Error,
    VolunteerSchemaCreate,
)
from django.shortcuts import get_object_or_404
from django.db.models import Avg, F
from api.utils import hours_diff
from api.google_forms import GoogleFormConnector, Form, Responses

google_creds = Path("svc-acc.json")

if not google_creds.exists:
    raise ValueError("Have you put `svc-acc.json` at root/server/svc-acc.json?")

app = NinjaExtraAPI()
gfc = GoogleFormConnector(google_creds)


@api_controller("volunteers/", tags=["Volunteers"], permissions=[])
class VolunteerController:
    @route.get("/", response=List[VolunteerSchema])
    def get_volunteers(self):
        return Volunteer.objects.all()

    @route.get("{id}", response=VolunteerSchema)
    def get_volunteer(self, id: str):
        volunteer = get_object_or_404(Volunteer, id=id)
        return volunteer

    @route.delete("{id}", response=Success)
    def delete_volunteer(self, id: uuid.UUID):
        volunteer = get_object_or_404(Volunteer, id=id)
        volunteer.delete()
        return Success(status_code=200)

    @route.post("/", response={200: VolunteerSchema, 404: Error})
    def create_volunteer(self, props: VolunteerSchemaCreate):
        props = props.model_dump()
        volunteer = Volunteer.objects.create(**props)
        return volunteer

    @route.get("{id}/events", response=VolunteerContributionsSchema)
    def get_events_by_volunteer(self, id: str):
        volunteer = get_object_or_404(Volunteer, id=id)
        events = volunteer.events.all()
        hours = 0
        for event in events:
            hours += hours_diff(end_time=event.end_time, start_time=event.start_time)

        return VolunteerContributionsSchema(events=events, hours=hours)


@api_controller("events/", tags=["Events"], permissions=[])
class EventController:
    @route.get("/", response=List[EventSchemaWithoutVolunteers])
    def get_events(
        self,
        location: Optional[str] = None,
        before_date: Optional[_dt.date] = None,
    ):
        Q = Event.objects.all()
        if location:
            Q = Q.filter(location=location)
        if before_date:
            Q = Q.filter(date__lt=before_date)
        return Q

    @route.get("{slug}", response=EventSchemaWithoutVolunteers)
    def get_event(self, slug: str):
        event = get_object_or_404(Event, slug=slug)
        return event

    @route.get("{slug}/volunteers", response=List[VolunteerSchema])
    def get_event_volunteers(self, slug: str):
        event = get_object_or_404(Event, slug=slug)
        return event.volunteers

    @route.post("/", response=EventSchemaWithoutVolunteers)
    def create_event(self, props: EventSchemaCreate):
        props = props.model_dump()
        event = Event.objects.create(**props)
        return event

    @route.post("{slug}", response=EventSchemaWithoutVolunteers)
    def update_event(self, slug: str, props: EventSchemaUpdate):
        props = props.model_dump()
        _ = Event.objects.filter(slug=slug).update(
            google_form_url=props["google_form_url"]
        )
        return get_object_or_404(Event, slug=slug)

    @route.post("{slug}/volunteers", response=VolunteerSchema)
    def add_volunteer_to_event(self, slug: str, volunteer_id: str):
        if not volunteer_id:
            return 404, "You must specify which Volunteer you want to add!"

        volunteer = get_object_or_404(Volunteer, id=volunteer_id)

        if not volunteer:
            return (
                404,
                "You cannot add a Volunteer that does not exist! Create the Volunteer first before calling this endpoint!",
            )
        event = get_object_or_404(Event, slug=slug)

        # update event.volunteers
        new_volunteers = [*event.volunteers.all(), volunteer]
        event.volunteers.set(new_volunteers)
        event.save()
        return volunteer


@api_controller("analytics/", tags=["Analytics"], permissions=[])
class AnalyticsController:
    @route.get("manhours", response=List[TimeseriesUnit])
    def get_manhours(
        self,
        event_slug: Optional[str] = None,
        location: Optional[str] = None,
        before_date: Optional[_dt.date] = datetime.now().date(),
    ):
        Q = Event.objects.all()
        if location:
            Q = Q.filter(location=location)
        if before_date:
            Q = Q.filter(date__lt=before_date)
        if event_slug:
            Q = Q.filter(slug=event_slug)

        res = defaultdict(lambda: 0)
        for event in Q.all():
            event_date = event.date
            event_volunteers = event.volunteers.all()
            total_hrs = hours_diff(
                end_time=event.end_time, start_time=event.start_time
            ) * len(event_volunteers)
            res[event_date] += total_hrs

        ts = []
        for date, hours in res.items():
            ts.append(TimeseriesUnit(date=date, metric=hours))
        return ts

    @route.get("volunteers", response=UniqueVolunteers)
    def get_unique_volunteers(
        self,
        event_slug: Optional[str] = None,
        location: Optional[str] = None,
        before_date: Optional[_dt.date] = datetime.now().date(),
    ):
        Q = Event.objects.all()
        if location:
            Q = Q.filter(location=location)
        if before_date:
            Q = Q.filter(date__lt=before_date)
        if event_slug:
            Q = Q.filter(slug=event_slug)

        res = set()
        for event in Q.all():
            volunteers = event.volunteers
            for volunteer in volunteers.all():
                res.add(volunteer.id)

        return UniqueVolunteers(unique_volunteers=len(res))

    @route.get("responses", response=List[FormResponseSchema])
    def get_form_responses(self, event_id: Optional[str] = None):
        Q = FormResponse.objects.all()
        if event_id:
            Q = Q.filter(event_id=event_id)
        return Q

    @route.get("satisfaction")
    def get_satisfaction(self):
        return list(
            FormResponse.objects.values(date=F("submit_date")).annotate(
                metric=Avg("satisfaction", default=0)
            )
        )


@api_controller("forms/", tags=["Google Forms Connector"], permissions=[])
class FormsController:
    @route.get("details/{form_id}", response=Form)
    def get_form_details(self, form_id: str):
        return gfc.fetch_form_details(form_id)

    @route.get("responses/{form_id}", response=Responses)
    def get_form_responses(self, form_id: str):
        return gfc.fetch_form_responses(form_id)

    @route.get("ai/{event_slug}/{form_id}", response=List[FormResponseSchema])
    def get_processed_responses(self, event_slug: str, form_id: str):
        processed_responses = gfc.process_responses(form_id)
        _ = FormResponse.objects.bulk_create(
            [
                FormResponse(event=Event.objects.get(slug=event_slug), **r.model_dump())
                for r in processed_responses
            ]
        )
        return processed_responses


@api_controller("responses/", tags=["Processed Google Form Responses"], permissions=[])
class ResponsesController:
    @route.get("{event_slug}", response=List[FormResponseSchema])
    def get_responses(self, event_slug: str):
        event = get_object_or_404(Event, slug=event_slug)
        return FormResponse.objects.filter(event=event).all()


app.register_controllers(
    VolunteerController,
    EventController,
    AnalyticsController,
    FormsController,
    ResponsesController,
)
