from django.shortcuts import render
# from django.http import HttpResponse

from .models import Product

from django.views.generic import ListView

# from django.contrib import messages
# from .forms import add_new_product_form

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


# def add_new_product(request):
#     if request.method == 'POST':
#         form = add_new_product_form(request.POST)
#         if form.is_valid():
#             form.save()
#             product_name = form.cleaned_data.get('product_name')
#             messages.success(request, f'Added product {product_name}!')
    # else:
    #     form = add_new_product_form()

class ItemListView(ListView):
    model = Product
    template_name = 'inventory/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'items'   #changing variable name to let it know, we stored in 'items' variable
    ordering = ['-date_posted'] #order from newest added to oldest