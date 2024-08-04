from django.shortcuts import render 

from store.models.customer import Customer
from django.views import  View
from store.models.product import Products


class Payment(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'payment.html' , {'products' : products} )
    def post(self , request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'payment.html' , {'products' : products} )
   
    
