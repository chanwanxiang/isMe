from django.conf.urls import url
from books.views import index

urlpatterns = [
    url(r'^index/$',index),
]