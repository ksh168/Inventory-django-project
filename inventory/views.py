from django.shortcuts import render, redirect, get_object_or_404

# from inventory.documents import ProductDocument
# from django.http import HttpResponse

from .models import Product

from django.views.generic import ListView, CreateView

from django.contrib import messages
from .forms import add_new_product_form


from rest_framework import viewsets
from .models import Product
from .serializers import *


from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    OrderingFilterBackend
)
from .documents import *


# dummy data
# items = [
#     {
#         'product_name': 'Sanitizier',
#         'price': 50,
#         'quantity': 2,
#         'date_posted': 'Jan 25 2022'
#     },
#     {
#         'product_name': 'Cup',
#         'price': 30,
#         'quantity': 5,
#         'date_posted': 'Jan 25 2022'
#     }
# ]


def home(request):
    # dictionary to put our data
    context = {
        'items': Product.objects.all()
    }
    # form = add_new_product_form()
    return render(request, 'inventory/home.html', context)
    # return render(request, 'inventory/home.html', context, {'form': form})


def about(request):
    return render(request, 'inventory/about.html', {'title': 'About'})


# def add_new_product(request):
#     if request.method == 'POST':
#         form = add_new_product_form(request.POST)
#         if form.is_valid():
#             form.save() #saves to db
#             product_name = form.cleaned_data.get('product_name')
#             messages.success(request, f'Added product {product_name}!')

#         # form = add_new_product_form()
#     else:
#         form = add_new_product_form()

#     return redirect('inventory-home')
#     # context = {
    #     'items': Product.objects.all()
    # }
    # return render(request, 'inventory/home.html', context)


class ItemListView(ListView):
    model = Product
    template_name = 'inventory/home.html'  # <app>/<model>_<viewtype>.html
    # changing variable name to let it know, we stored in 'items' variable
    context_object_name = 'items'
    ordering = ['-date_posted']  # order from newest added to oldest


# class ItemCreateView(CreateView):
#     model = Product
#     fields = ['product_name', 'price', 'quantity']
#     # context['form'] = form


# for rest_framework api
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#####
# for elasticsearch
# class PublisherDocumentView(DocumentViewSet):
#     document = ProductDocument
#     serializer_class = ProductDocumentSerializer

#     lookup_field = 'product_name'
#     fielddata = True

#     filter_backends = [
#         FilteringFilterBackend,
#         CompoundSearchFilterBackend,
#         # OrderingFilterBackend
#     ]

#     search_fields = 'product_name'
#     multi_match_search_fields = 'product_name'

#     filter_fields = {
#         'product_name': 'product_name'
#     }

    # # ordering_fields = {
    # #     'id': None,
    # # }
    # # ordering = ('id',)


# not getting used currently
# class ProfileDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'profile_detail.html'

#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product)
#         return Response({'serializer': serializer, 'product': product})

#     def post(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'product': product})
#         serializer.save()
#         return redirect('inventory-home')
