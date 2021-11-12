from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.deletion import CASCADE, DO_NOTHING

from api_login.models import Person


class DogSize(models.Model):
    dog_size_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)


class Dogs(models.Model):
    dog_id = models.AutoField(primary_key=True)
    dogsize = models.ForeignKey(DogSize, to_field='dog_size_id', null=True, on_delete=DO_NOTHING)
    dog_name = models.CharField(max_length=50, null=True)
    person = models.ForeignKey(Person, to_field='person_id', null=True, on_delete=CASCADE)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)


class Walker(models.Model):
    walker_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Person, to_field='user_id', null=True, on_delete=CASCADE)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)


class EventCalendar(models.Model):
    event_calendar_id = models.AutoField(primary_key=True)
    walker = models.ForeignKey(Walker, to_field='walker_id', null=True, on_delete=CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)


class WalkerxDog(models.Model):
    walker_id = models.IntegerField(null=True)
    dog_id = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
