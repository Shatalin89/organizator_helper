from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vk_id = models.CharField(max_length=30, blank=True)
    num_telephone = PhoneNumberField(blank=True)
    date_birthday = models.DateField(blank=True)
    middle_name = models.CharField(max_length=30, blank=True)

    def get_fio(self):
        return '{0} {1}.{2}'.format(self.user.last_name, self.user.first_name[:1], self.middle_name[:1])






