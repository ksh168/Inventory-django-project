from django import forms
from .models import Product

class add_new_product_form(forms.ModelForm):
    product_name = forms.CharField()
    price = forms.IntegerField()
    quantity = forms.IntegerField()

    class Meta:
        model = Product
        fields = ['product_name', 'price', 'quantity']
