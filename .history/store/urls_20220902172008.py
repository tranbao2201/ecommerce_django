
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from greatkart.settings import MEDIA_ROOT
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
