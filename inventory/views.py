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

import json

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




from django.views import View
from django.http import JsonResponse
import json


# to bypass CSRF
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')  # to bypass CSRF
class ShoppingCart(View):
        # GET method
    def get(self, request):
        # MAX_OBJECTS = 20

        #search functionality
        q = request.GET.get('q')
        if q:
            items = Product.objects.filter(product_name__icontains=q)
            items_count = items.count()

        #if q parameter not passed, return all
        else:
            items_count = Product.objects.count()
            items = Product.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'product_name': item.product_name,
                'price': item.price,
                'quantity': item.quantity,
            })

        # reply = {
        #     'count': items_count,  # total count of items in DB
        #     'items': items_data
        # }

        # reply = items_data

        # return JsonResponse(reply, safe=False)
        # return json.dumps(reply)

        context = {
        'items': items
        }
        # form = add_new_product_form()
        return render(request, 'inventory/home1.html', context)


        
    # POST method
    def post(self, request):
        # Using the json module, we've decoded and parsed the incoming request's body into an object we can work with
        data = json.loads(request.body.decode("utf-8"))

        p_name = data.get('product_name')
        p_price = data.get('price')
        p_quantity = data.get('quantity')

        # dictionary to hold fields and their values
        product_data = {
            'product_name': p_name,
            'price': p_price,
            'quantity': p_quantity,
        }

        # persisted a Product to our database, via the create() method of the Model class, filling it with our product_data
        cart_item = Product.objects.create(
            **product_data)  # similar to **kwargs
       
        reply = {
            "message": f"New Item: {cart_item.product_name} added to Cart with id: {cart_item.id}"
        }

        # convert Python dictionary to a valid JSON object that is sent over HTTP back to the client
        return JsonResponse(reply, status=201)        # HTTP 201 Created success status



@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCartUpdate(View):
    # PATCH method->to change one of the attributes
    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        # get item from DB
        item = Product.objects.get(id=item_id)

        # currently allowing to change quantity only
        item.quantity = data['quantity']

        # save changes to DB
        item.save()

        reply = {
            'message': f"Item: {item.product_name} with id {item_id} has been updated with new quantity as {item.quantity}"
        }
        return JsonResponse(reply)

    #DELETE method
    def delete(self, request, item_id):
        item = Product.objects.get(id=item_id)
        item.delete()

        reply = {
            'message': f'Item: {item.product_name} with id {item_id} has been deleted'
        }

        return JsonResponse(reply)


#search trial
# from django.http import JsonResponse

# def search_api(request):
#     q = request.GET.get("q")
#     results = []
#     if q:
#         results = [{
#             "id": a.id,
#             "title": a.title
#         } for a in Article.objects.filter(title__icontains=q)]
#     return JsonResponse(results)




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
