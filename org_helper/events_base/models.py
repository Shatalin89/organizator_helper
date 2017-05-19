from django.db import models
from clients_base.models import Clients
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class Hall(models.Model):
    class Meta:
        db_table = 'hall'
    hall_name = models.CharField(max_length = 100)
    hall_address = models.CharField(max_length = 100, blank = True)
    hall_max_places = models.IntegerField(default=10, blank = True, null=True)
    hall_phone = PhoneNumberField(blank=True, null=True)
    hall_price_in_hour = models.IntegerField(blank=True, null=True)
    hall_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.hall_name


class Shows(models.Model):
    class Meta:
        db_table = 'shows'
    shows_names = models.CharField(max_length=100)
    shows_time_length = models.TimeField(default='01:00', blank=True)
    shows_description = models.CharField(max_length=400, blank=True, null=True)
    shows_image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.shows_name


class EventsInfo(models.Model):
    class Meta:
        db_table = 'events'

    events_show_name = models.ForeignKey(Shows)
    events_date_time = models.DateTimeField(default=timezone.now)
    event_place_count = models.IntegerField(default=15)
    event_vk_url = models.URLField(blank=True, null=True)



class EventPlace(models.Model):
    class Meta:
        db_table = 'eventplace'
    event = models.ForeignKey(EventsInfo)
    client = models.ForeignKey(Clients, blank=True, null=True)
    place_price = models.IntegerField(default=1)
    place_status = models.CharField(max_length=4, default='FREE')
    date_add = models.DateTimeField(default=timezone.now())
    date_change = models.DateTimeField()
    comment = models.TextField(max_length=500)