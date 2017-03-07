from django.conf.urls import url
from . import views

urlpatterns = [
    # /dxxcodecoverage
    url(r'^$', views.index, name="index"),

    # /dxxcodecoverage/21/
    url(r'^(?P<album_id>[0-9]+)/$' , views.detail, name='detail'),
]
