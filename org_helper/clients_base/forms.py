from django import forms
from . import models


class ClientForm(forms.ModelForm):

    last_name = forms.CharField(label=u'Фамилия',
                                 widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-control'}))
    first_name = forms.CharField(label=u'Имя',
                                 widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    middle_name = forms.CharField(label=u'Отчество',
                                 widget=forms.TextInput(attrs={'placeholder': 'Отчество', 'class': 'form-control'}))
    date_birthday = forms.DateField(label=u'Дата рождения',
                                 widget=forms.DateInput(attrs={'class': 'form-control date',
                                                              'id': 'datetimepicker1'}))
    phone = forms.CharField(label=u'Телефон', widget=forms.TextInput(attrs={'class': 'form-control bfh-phone',
                                                                            'data-format': '+7 (ddd) ddd-dddd',
                                                                            'pattern': '(\+[\d\ \(\)\-]{16})',
                                                                            'type':'tel'}))
    email = forms.CharField(label=u'Почта',
                            widget=forms.TextInput(attrs={'placeholder': 'Почта',
                                                            'class': 'form-control',
                                                            'type': 'email'}))
    description = forms.CharField(label=u'О клиенте',
                                 widget=forms.Textarea(attrs={'placeholder': 'Комментарий о клиенте', 'class': 'form-control'}))
    vk_id = forms.URLField(label=u'ссылка на ВК',
                                 widget=forms.URLInput(attrs={'placeholder': 'vk.com', 'class': 'form-control'}))
    fb_id = forms.URLField(label=u'ссылка на FB',
                                 widget=forms.URLInput(attrs={'placeholder': 'facebook.com', 'class': 'form-control'}))
    insta_id = forms.URLField(label=u'Ссылка в истаграмм',
                                 widget=forms.URLInput(attrs={'placeholder': 'instagram.com', 'class': 'form-control'}))

    class Meta:
        model = models.Clients
        exclude = ['date_add']
