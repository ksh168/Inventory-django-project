from django.urls import path, include

from .views import ItemListView

from . import views

from rest_framework import routers


router = routers.DefaultRouter()    #inherit from rest_framework
router.register('inventory', views.ProductView)


urlpatterns = [
    path('', ItemListView.as_view(), name='inventory-home'),
    path('about/', views.about, name='inventory-about'),
    # path('add_new_product/', views.add_new_product, name='inventory-add'),
    path('api/', include(router.urls)),
]
