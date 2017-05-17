from django.db import models
from clients_base.models import Clients
from phonenumber_field.modelfields import PhoneNumberField


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
    shows_name = models.CharField(max_length = 100)
    shows_time_length = models.TimeField(default='01:00')
    shows_description = models.TimeField(blank=True, null=True)