import datetime as _dt
from collections import defaultdict
from datetime import datetime
from typing import List, Optional
from ninja_extra import NinjaExtraAPI, api_controller, route
from api.models import Volunteer, Event
from api.schemas import (
    ManhoursUnit,
    UniqueVolunteers,
    VolunteerContributionsSchema,
    VolunteerSchema,
    EventSchemaWithoutVolunteers,
    Error,
)
from django.shortcuts import get_object_or_404

from api.utils import hours_diff

app = NinjaExtraAPI()


@api_controller("volunteers/", tags=["Volunteers"], permissions=[])
class VolunteerController:
    @route.get("/", response=List[VolunteerSchema])
    def get_volunteers(self):
        return Volunteer.objects.all()

    @route.get("{id}", response=VolunteerSchema)
    def get_volunteer(self, id: str):
        volunteer = get_object_or_404(Volunteer, id=id)
        return volunteer

    @route.post("/", response={200: VolunteerSchema, 404: Error})
    def create_volunteer(self, props: VolunteerSchema):
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
    def create_event(self, props: EventSchemaWithoutVolunteers):
        props = props.model_dump()
        event = Event.objects.create(**props)
        return event

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
    @route.get("manhours", response=List[ManhoursUnit])
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
            total_hrs = hours_diff(end_time=event.end_time, start_time=event.start_time)
            res[event_date] += total_hrs

        ts = []
        for date, hours in res.items():
            ts.append(ManhoursUnit(date=date, hours=hours))
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


app.register_controllers(VolunteerController, EventController, AnalyticsController)
