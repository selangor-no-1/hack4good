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


class ManhoursUnit(Schema):
    date: _dt.date
    hours: int | float


class Error(Schema):
    message: str
