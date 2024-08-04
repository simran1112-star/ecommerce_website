from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        print(customer)
        orders = Order.get_orders_by_customer(customer)
        print("ye rahe orders:",orders)
        return render(request , 'orders.html'  , {'orders' : orders})
    def post(self, request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Products.get_products_by_id(ids)
        print("adsfas",products)
        return redirect("orders")
