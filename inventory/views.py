from django.shortcuts import render
# from django.http import HttpResponse

from .models import Product


#dummy data
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
    #dictionary to put our data
    context = {
        'items': Product.objects.all()
    }
    return render(request, 'inventory/home.html', context)

def about(request):
    return render(request, 'inventory/about.html', {'title': 'About'})