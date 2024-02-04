import datetime as _dt
from typing import List
from ninja import Schema, ModelSchema
from api.models import Volunteer, Event


class VolunteerSchema(ModelSchema):
    class Meta:
        model = Volunteer
        fields = ("id", "name", "date_of_birth", "email", "contact_number")


class EventSchemaWithoutVolunteers(ModelSchema):
    # volunteers: List[VolunteerSchema]

    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "slug",
            "location",
            "description",
            "image",
            "date",
            "start_time",
            "end_time",
        )


class VolunteerContributionsSchema(Schema):
    events: List[EventSchemaWithoutVolunteers]
    hours: int | float


class TimeseriesUnit(Schema):
    date: _dt.date


class ManhoursUnit(TimeseriesUnit):
    hours: int | float


class UniqueVolunteers(Schema):
    unique_volunteers: int


class Error(Schema):
    message: str
