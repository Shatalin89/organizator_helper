from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.get_halls, name='halls'),
    url(r'^add/$', views.add_hall, name='hall'),
    #url(r'^edit/(?P<clients_id>\d+)/$', views.edit_client, name='edit_client'),
    #url(r'^del/(?P<clients_id>\d+)/$', views.del_client, name='del_client'),
]