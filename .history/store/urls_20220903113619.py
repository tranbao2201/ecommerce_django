from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:category_id>', views.store, name='products'),
]
