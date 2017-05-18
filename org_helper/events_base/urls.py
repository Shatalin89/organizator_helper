from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^halls/$', views.get_halls, name='halls'),
    url(r'^halls/add/$', views.add_hall, name='hall'),
    url(r'^halls/edit/(?P<hall_id>\d+)/$', views.edit_hall, name='edit_hall'),
    url(r'^halls/del/(?P<hall_id>\d+)/$', views.del_hall, name='del_hall'),

    url(r'^shows/$', views.get_shows, name='shows'),
    url(r'^shows/add/$', views.add_show, name='show'),
    url(r'^shows/edit/(?P<show_id>\d+)/$', views.edit_show, name='edit_show'),
    url(r'^shows/del/(?P<show_id>\d+)/$', views.del_show, name='del_show'),

]