from django import forms
from . import models
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class ClientForm(forms.ModelForm):
    last_name = forms.CharField(label=u'Фамилия',
                                 widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-control'}))
    first_name = forms.CharField(label=u'Имя',
                                 widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    middle_name = forms.CharField(label=u'Отчество',
                                 widget=forms.TextInput(attrs={'placeholder': 'Отчество', 'class': 'form-control'}))
    date_birthday = forms.DateField(label=u'Дата рождения',
                                 widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))
    phone = forms.CharField(label=u'Телефон', widget=forms.TextInput(attrs={'class': 'form-control input-medium bfh-phone','data-format': '+1 (ddd) ddd-dddd'}))
    email = forms.CharField(label=u'Почта',
                                 widget=forms.TextInput(attrs={'placeholder': 'Почта', 'class': 'form-control'}))
    description = forms.CharField(label=u'О клиенте',
                                 widget=forms.Textarea(attrs={'placeholder': 'Комментарий о клиенте', 'class': 'form-control'}))
    vk_id = forms.CharField(label=u'ссылка на ВК',
                                 widget=forms.TextInput(attrs={'placeholder': 'vk.com', 'class': 'form-control'}))
    fb_id = forms.CharField(label=u'ссылка на FB',
                                 widget=forms.TextInput(attrs={'placeholder': 'facebook.com', 'class': 'form-control'}))
    insta_id = forms.CharField(label=u'Ссылка в истаграмм',
                                 widget=forms.TextInput(attrs={'placeholder': 'instagram.com', 'class': 'form-control'}))
    class Meta:
        model = models.Clients
        exclude = ['date_add']
