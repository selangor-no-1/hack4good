from typing import List
from ninja_extra import NinjaExtraAPI, api_controller, route
from api.models import Volunteer, Event
from api.schemas import VolunteerSchema, EventSchema, Error
from django.shortcuts import get_object_or_404

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


@api_controller("events/", tags=["Events"], permissions=[])
class EventController:
    @route.get("/", response=List[EventSchema])
    def get_events(self):
        return Event.objects.all()

    @route.get("{slug}", response=EventSchema)
    def get_event(self, slug: str):
        event = get_object_or_404(Event, slug=slug)
        return event

    @route.post("/", response=EventSchema)
    def create_event(self, props: EventSchema):
        props = props.model_dump()
        event = Event.objects.create(**props)
        return event


@api_controller("analytics/", tags=["Analytics"], permissions=[])
class AnalyticsController:
    ...


app.register_controllers(VolunteerController, EventController, AnalyticsController)
