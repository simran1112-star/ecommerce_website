from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from store.models.Subcategory import Subcategory
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        print(cart)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        print(f"currently at: {request.get_full_path()[1:]}")

        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
def store(request):
    cart = request.session.get('cart', {})
    categories = Category.get_all_categories()
    subcategories = Subcategory.get_all_subcategories()
    selected_category_id = request.GET.get('category')
    selected_subcategory_id = request.GET.get('subcategory')

    template_name = 'index.html'

    if selected_subcategory_id:
        key=False
        products = Products.get_all_products_by_subcategory_id(selected_subcategory_id)
        data = {
            'products': products,
            'categories': categories,
            'subcategories': subcategories,
            'selected_category_id': selected_category_id,
            'selected_subcategory_id': selected_subcategory_id,
            'cart': cart,
        }
        return render(request, template_name, data)

    elif selected_category_id:
        key=False
        products = Products.get_all_products_by_categoryid(selected_category_id)
    else:
        key=True
        products = []

    print('Selected Category ID:', selected_category_id)
    print('Selected Subcategory ID:', selected_subcategory_id)
    print('Number of Products:', len(products))
    print(products)

    data = {
        "key":key,
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
        'selected_category_id': selected_category_id,
        'selected_subcategory_id': selected_subcategory_id,
        'cart': cart,
    }

    print('you are:', request.session.get('email'))
    return render(request, template_name, data)
