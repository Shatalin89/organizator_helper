from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    date_birthday = models.DateField(blank=True)
    phone = PhoneNumberField(blank=True)
    vk_id = models.URLField(blank=True)
    fb_id = models.URLField(blank=True)
    insta_id = models.URLField(blank=True)

    def get_fio(self):
        return '{0} {1}.{2}.'.format(self.last_name, self.first_name[:1], self.middle_name[:1])






