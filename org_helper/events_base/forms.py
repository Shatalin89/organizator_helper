from django import forms
from . import models


class HallForm(forms.ModelForm):
    hall_name = forms.CharField(label=u'Название',
                                 widget=forms.TextInput(attrs={'placeholder': 'Название зала', 'class': 'form-control'}))
    hall_address = forms.CharField(label=u'адрес',
                                 widget=forms.TextInput(attrs={'placeholder': 'Адрес', 'class': 'form-control'}))
    hall_max_places = forms.CharField(label=u'Вместимость',
                                 widget=forms.TextInput(attrs={'placeholder': 'кол-во. мест', 'class': 'form-control'}))

    hall_phone = forms.CharField(label=u'Телефон', widget=forms.TextInput(attrs={'class': 'form-control bfh-phone',
                                                                            'data-format': '+7 (ddd) ddd-dddd',
                                                                            'pattern': '(\+[\d\ \(\)\-]{16})',
                                                                            'type':'tel'}))
    hall_price_in_hour = forms.CharField(label=u'Стоимость часа',
                                 widget=forms.TextInput(attrs={'placeholder': 'руб/ч', 'class': 'form-control'}))
    hall_url = forms.URLField(label=u'Сайт', widget=forms.URLInput(attrs={'placeholder': 'http://', 'class': 'form-control'}))

    class Meta:
        model = models.Hall
        exclude = []

class ShowForm(forms.ModelForm):
    shows_name = forms.CharField(label=u'Название', widget=forms.TextInput(attrs={'placeholder': 'Название', 'class': 'form-control'}))
    shows_time_length = forms.CharField(label=u'Длительность', widget=forms.TextInput(attrs={'class': 'form-controlglyphicon glyphicon-calendar'}))
    shows_description = forms.CharField(label=u'Описание',
                                 widget=forms.Textarea(attrs={'placeholder': 'Описание', 'class': 'form-control'}))
    shows_image = forms.ImageField(label=u'Афиша',widget=forms.FileInput(attrs={'placeholder': 'Афиша', 'class': 'btn btn-secondary'}))

    class Meta:
        model = models.Shows
        exclude = []
