import uuid
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Event(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name")
    description = models.CharField(max_length=2000, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    volunteers = models.ManyToManyField("Volunteer", related_name="events", blank=True)

    def __str__(self):
        return f"Event(name={self.name})"


class Volunteer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"Volunteer(name={self.name})"


class FormResponse(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    email = models.EmailField(null=True, blank=True)
    content = models.CharField(max_length=5000)
    satisfaction = models.IntegerField()
    reason = models.CharField(max_length=1000)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Volunteer(id={id})"
