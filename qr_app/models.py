from django.db import models
from django.utils import timezone
# Create your models here.
class Resident(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    uid = models.TextField(blank=False, null=False)
    pw = models.TextField(blank=False, null=False)
    name = models.CharField(max_length=10, blank=True, null=True)
    birth_year = models.IntegerField()

class Device(models.Model):
    MOBILE = 'mb'
    TABLET = 'tl'
    PC = 'pc'
    TYPE_CHOICES = [
        (MOBILE, '모바일'),
        (TABLET, '테블릿'),
        (PC, 'pc')
    ]
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    device_type = models.CharField(
        max_length=10, 
        choices=TYPE_CHOICES,
        default=MOBILE
    )
    os = models.CharField(max_length=10, blank=True)
    version = models.CharField(max_length=10, blank=True)

class Visitor(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(default=timezone.now)
    time = models.DurationField()
    visited = models.BooleanField(default=False)

class EntranceLog(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    visitor_idx = models.ForeignKey(Visitor, models.DO_NOTHING, db_column='visitor_idx')

class Building(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

class Floor(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

class Room(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

class Apartment(models.Model):
    objects = models.Manager()
    building = models.ForeignKey(Building, on_delete = models.CASCADE, blank=True)
    floor = models.ForeignKey(Floor, on_delete = models.CASCADE, blank=True)
    room = models.ForeignKey(Room, on_delete = models.CASCADE, blank=True)

