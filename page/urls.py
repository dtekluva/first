

from django.conf.urls import url
from page import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<mentor_id>[0-9]+)$', views.detail, name= 'detail'),
]
