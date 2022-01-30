import json
from rest_framework import serializers
from .models import Product

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import *

#for django rest_framework
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url', 'id', 'product_name',
                  'price', 'quantity', 'date_posted')


#####
# for elasticsearch
# class ProductDocumentSerializer(DocumentSerializer):
#     class Meta:
#         model = Product
#         document = ProductDocument

#         fields = ('product_name', 'price', 'quantity')

#         def get_location(self, obj):
#             """Represent location value."""
#             try:
#                 return obj.location.to_dict()
#             except:
#                 return {}
