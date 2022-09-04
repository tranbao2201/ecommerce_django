
from django.urls import path

from greatkart.settings import MEDIA_ROOT
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
