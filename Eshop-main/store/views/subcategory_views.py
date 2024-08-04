# views/subcategory_views.py

from django.shortcuts import render
from django.views import View
from store.models.Subcategory import Subcategory

class SubcategoryView(View):
    template_name = 'subcategories.html'

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category')
        products=request.GET.get('products')
        print(category_id)
        subcategories = Subcategory.objects.filter(category_id=category_id)
        print(subcategories)
        

        context = {
            'products':products,'subcategories': subcategories}
        print(context)
        return render(request, self.template_name, context)
