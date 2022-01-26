from django.urls import path

from .views import ItemListView

from . import views

urlpatterns = [
    path('', ItemListView.as_view(), name='inventory-home'),
    path('about/', views.about, name='inventory-about'),
]
