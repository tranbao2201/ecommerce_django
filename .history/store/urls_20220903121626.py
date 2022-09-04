from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:category_id>', views.store, name='products_by_category'),
    path('<int:category_id>', views.store, name='products_by_category'),
    path('<int:pr>', views.store, name='products_by_category'),
]
