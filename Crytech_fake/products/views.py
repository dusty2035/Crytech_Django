from django.shortcuts import render , get_object_or_404
from .models import Product
# Create your views here.

def product(request):
    product = Product.objects
    return render(request , 'products.html' , {'product' : product})


def product_s(request , product_id):
    product_s = get_object_or_404(Product , pk=product_id)
    return render(request, 'product.html' , {'product_s' : product_s})