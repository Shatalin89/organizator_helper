from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.utils import timezone

class Clients(models.Model):

    class Meta:
        db_table = 'clients'
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    date_birthday = models.DateField(blank=True)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    description = models.TextField(max_length=300, blank=True)
    vk_id = models.URLField(blank=True, null=True)
    fb_id = models.URLField(blank=True, null=True)
    insta_id = models.URLField(blank=True, null=True)
    date_add = models.DateTimeField(default=timezone.now)

    def get_fio(self):
        return '{0} {1}.{2}.'.format(self.last_name, self.first_name[:1], self.middle_name[:1])






