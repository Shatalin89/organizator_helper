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

    url(r'^info/$', views.get_info, name='events'),
    url(r'^info/add/$', views.add_info, name='event'),
    url(r'^info/edit/(?P<info_id>\d+)/$', views.edit_info, name='edit_event'),
    url(r'^info/del/(?P<info_id>\d+)/$', views.del_info, name='del_event'),

    url(r'^reg/$', views.add_reg, name='reg_client'),
    #url(r'^reg/$', views.RegCLient.as_view(), name='reg_client'),

]