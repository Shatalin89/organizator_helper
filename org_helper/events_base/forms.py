from django import forms
from . import models
from clients_base.models import Clients
from djmoney.models.fields import MoneyField

class HallForm(forms.ModelForm):
    hall_name = forms.CharField(label=u'Название',
                                 widget=forms.TextInput(attrs={'placeholder': 'Название зала', 'class': 'form-control'}))
    hall_address = forms.CharField(label=u'Адрес', required = False,
                                 widget=forms.TextInput(attrs={'placeholder': 'ул. Советская, д. 12, оф. 14', 'class': 'form-control'}))
    hall_max_places = forms.CharField(label=u'Вместимость',required = False,
                                 widget=forms.TextInput(attrs={'placeholder': 'кол-во. мест', 'class': 'form-control'}))

    hall_phone = forms.CharField(label=u'Телефон',required = False, widget=forms.TextInput(attrs={'class': 'form-control bfh-phone',
                                                                            'data-format': '+7 (ddd) ddd-dddd',
                                                                            'pattern': '(\+[\d\ \(\)\-]{16})',
                                                                            'type':'tel'}))
    hall_price_in_hour = forms.CharField(label=u'Стоимость часа', required = False,
                                 widget=forms.TextInput(attrs={'placeholder': 'руб/ч', 'class': 'form-control'}))
    hall_url = forms.URLField(label=u'Сайт',required = False, widget=forms.URLInput(attrs={'placeholder': 'http://', 'class': 'form-control'}))

    class Meta:
        model = models.Hall
        exclude = []

class ShowForm(forms.ModelForm):
    shows_names = forms.CharField(label=u'Название', widget=forms.TextInput(attrs={'placeholder': 'Название', 'class': 'form-control'}))
    shows_time_length = forms.CharField(label=u'Длительность',required = False, widget=forms.TimeInput(format=('%H:%m'),attrs={}))
    shows_description = forms.CharField(label=u'Описание', required = False,
                                 widget=forms.Textarea(attrs={'placeholder': 'Описание', 'class': 'form-control'}))
    shows_image = forms.ImageField(label=u'Афиша', required = False, widget=forms.FileInput(attrs={'placeholder': 'Афиша', 'class': 'btn btn-secondary'}))

    class Meta:
        model = models.Shows
        exclude = []


class EventForm(forms.ModelForm):
    class Meta:
        model = models.EventsInfo
        exclude = []


class EventRegForm(forms.ModelForm):
    CLIENTS_LIST= [[i.pk, i.get_fio_phone] for i in Clients.objects.all()]
    EVENT_LIST=[[i.pk, i.get_event] for i in models.EventsInfo.objects.filter(event_state=True)]
    PLACE_STATUS = (('FREE', 'Свободно'), ('BRON', 'Предварительная запись'), ('RESV', 'Пред. оплата'), ('SOLD', 'Оплачено'))

    event = forms.MultipleChoiceField(label='Мероприятия', required=False, widget=forms.CheckboxSelectMultiple, choices=EVENT_LIST)
    client = forms.MultipleChoiceField(label='Клиенты', required=False, widget=forms.CheckboxSelectMultiple, choices=CLIENTS_LIST)
    place_status = forms.ChoiceField(choices=PLACE_STATUS)
    comment = forms.CharField(required = False, widget=forms.Textarea)
    place_price = MoneyField(max_digits=10, decimal_places=2, default_currency='RUB')
    class Meta:
        model = models.EventPlace

        exclude = ['date_add', 'date_change', 'place_status']

