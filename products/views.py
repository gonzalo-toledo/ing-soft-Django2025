from django.shortcuts import render, get_object_or_404

from products.services.products import ProductService
from products.services.customers import CustomerService
from products.services.orders import OrderService

from products.models import Product

# Create your views here.

def product_list(request):
    all_products = ProductService.get_all()
    total_price = ProductService.sum_total_price(all_products)
    
    return render(request, 
            'products/list.html',
            {
                'products': all_products,
                'total_price':total_price, 
            })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request,
            'products/detail.html',
            {
                'product': product,
            })

def order_list(request):
    all_orders = OrderService.get_all()
    return render(request, 
            'orders/list.html',
            {
                'orders': all_orders,
            }
            )
    
def customer_list(request):
    all_customers = CustomerService.get_all()
    return render (request,
                'customers/list.html',
                {
                    'customers': all_customers,
                })