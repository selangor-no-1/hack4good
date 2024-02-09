import datetime as _dt
from typing import List, Literal
from ninja import Schema, ModelSchema
from api.models import FormResponse, Volunteer, Event


class VolunteerSchema(ModelSchema):
    class Meta:
        model = Volunteer
        fields = (
            "id",
            "name",
            "date_of_birth",
            "date_created",
            "email",
            "contact_number",
        )


class EventSchemaWithoutVolunteers(ModelSchema):
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
            "google_form_url",
        )


class EventSchemaCreate(ModelSchema):
    class Meta:
        model = Event
        fields = (
            "name",
            "location",
            "description",
            "image",
            "date",
            "start_time",
            "end_time",
        )


class EventSchemaUpdate(Schema):
    google_form_url: str


class VolunteerSchemaCreate(ModelSchema):
    class Meta:
        model = Volunteer
        fields = ("name", "date_of_birth", "email", "contact_number")


class FormResponseSchema(ModelSchema):
    class Meta:
        model = FormResponse
        fields = (
            "id",
            "email",
            "submit_date",
            "content",
            "satisfaction",
            "reason",
        )


class VolunteerContributionsSchema(Schema):
    events: List[EventSchemaWithoutVolunteers]
    hours: int | float


class TimeseriesUnit(Schema):
    date: _dt.date | str
    metric: int | float


class UniqueVolunteers(Schema):
    unique_volunteers: int


class Error(Schema):
    message: str


class Success(Schema):
    status_code: int
