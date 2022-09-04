from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:category>', views.store, name='store'),
]
