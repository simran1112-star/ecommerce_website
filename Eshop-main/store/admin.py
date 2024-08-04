from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.Subcategory import Subcategory  # Update the import statement
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'subcategory']  # Update 'category' to 'subcategory'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Subcategory)
admin.site.register(Order)
