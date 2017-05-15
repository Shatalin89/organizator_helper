from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.get_clients, name='clients'),
    url(r'^add/$', views.add_client, name='client'),
]