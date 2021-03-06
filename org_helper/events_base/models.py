from django.db import models
from clients_base.models import Clients
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from djmoney.models.fields import MoneyField


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
        return self.shows_names


class EventsInfo(models.Model):
    class Meta:
        db_table = 'events'

    events_show_name = models.ForeignKey(Shows)
    events_hall = models.ForeignKey(Hall)
    events_date_time = models.DateTimeField(default=timezone.now)
    event_place_count = models.IntegerField(default=15)
    event_place_current_count = models.IntegerField(default=0)
    event_vk_url = models.URLField(blank=True, null=True)
    event_state = models.BooleanField(default=False)

    def get_event(self):
        return '{0} {1}'.format(self.events_show_name, self.events_date_time)

class EventPlace(models.Model):
    class Meta:
        db_table = 'eventplace'
    event = models.ForeignKey(EventsInfo)
    client = models.ForeignKey(Clients, blank=True, null=True)
    place_price = models.IntegerField(default=0)
    place_status = models.CharField(max_length=4, default='FREE')
    date_add = models.DateTimeField(default=timezone.now())
    date_change = models.DateTimeField()
    comment = models.TextField(max_length=500)