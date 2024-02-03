from typing import List
from ninja import Schema, ModelSchema
from api.models import Volunteer, Event


class VolunteerSchema(ModelSchema):
    class Meta:
        model = Volunteer
        fields = ("id", "name", "date_of_birth", "email", "contact_number")


class EventSchema(ModelSchema):
    volunteers: List[VolunteerSchema]

    class Meta:
        model = Event
        fields = ("id", "name", "slug", "description", "image", "date", "volunteers")


class Error(Schema):
    message: str
