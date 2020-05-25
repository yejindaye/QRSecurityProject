from django.db import models
from django.utils import timezone
# Create your models here.

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


class Building(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

    def __str__(self):
        return str(self.number) + "동"

class Floor(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

    def __str__(self):
        return str(self.number) + "층"

class Room(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

    def __str__(self):
        return str(self.number) + "호"

class Apartment(models.Model):
    objects = models.Manager()
    building = models.ForeignKey(Building, on_delete = models.CASCADE, blank=True)
    floor = models.ForeignKey(Floor, on_delete = models.CASCADE, blank=True)
    room = models.ForeignKey(Room, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return str(self.building.number)+"동 " + str(self.floor.number) + "0" + str(self.room.number)+"호"

class Resident(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    uid = models.TextField(blank=False, null=False)
    pw = models.TextField(blank=False, null=False)
    name = models.CharField(max_length=10, blank=True, null=True)
    birth_year = models.IntegerField()
    room = models.ForeignKey(Apartment, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return self.name

class Visitor(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(default=timezone.now)
    time = models.DurationField()
    visited = models.BooleanField(default=False)
    room = models.ForeignKey(Apartment, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return self.name

class EntranceLog(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    visitor_idx = models.ForeignKey(Visitor, models.DO_NOTHING, db_column='visitor_idx')
