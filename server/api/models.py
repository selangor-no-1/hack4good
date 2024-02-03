import uuid
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Event(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name")
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    volunteers = models.ManyToManyField("Volunteer", related_name="events", blank=True)

    def __str__(self):
        return f"Event(name={self.name})"


class Volunteer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=8)

    def __str__(self):
        return f"Volunteer(name={self.name})"
