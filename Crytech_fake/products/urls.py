from django.urls import path
from . import views

urlpatterns = [
    path('' , views.product , name ='products'),
    path('<int:product_id>/' , views.product_s , name = 'product')
]
