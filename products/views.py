from django.shortcuts import render #get_object_or_404
from django.contrib import messages

# from products.services.products import ProductService
from products.services.customers import CustomerService
from products.services.orders import OrderService

from products.models import Product, Order

# Create your views here.    
def customer_list(request):
    all_customers = CustomerService.get_all()
    return render (request,
                'customers/list.html',
                {
                    'customers': all_customers,
                })
    

    
# NUEVAS VISTAS BASADAS EN CLASES
# views.generic es un modulo de django que contiene vistas basadas en clases:
#ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views import View # no tienen tanto poder como views.generic. Mas enfocado a vistas de funciones
from django.views.generic import CreateView,DeleteView, DetailView, ListView
from django .urls import reverse_lazy 

from products.forms import ProdcutForm 
# from models import Product


class ProductList (ListView):
    model = Product # modelo a usar
    template_name = 'products/list.html' # template a usar en la vista
    context_object_name = 'products' # nombre del contexto a usar en el template

# DEPRECADO
# def product_list(request):
#     all_products = ProductService.get_all()
#     total_price = ProductService.sum_total_price(all_products)
    
#     return render(request, 
#             'products/list.html',
#             {
#                 'products': all_products,
#                 'total_price':total_price, #!RESOLVER ESTO!!
#             })

    
class ProductDetail (DetailView):
    model = Product 
    template_name = 'products/detail.html' 
    context_object_name = 'product'
    pk_url_kwarg = 'product_id' # nombre con el que va a buscar el ID en la url
    
# DEPRECADO
# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request,
#             'products/detail.html',
#             {
#                 'product': product,
#             })    

class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('product_list') # redirecciona a la lista de productos. 'pruduct_list' es el name de la url
    
    
class ProductCreateView(View):
    def get(self, request):
        return render (
            request,
            'products/create.html',
        ) 
    def post(self, request):
        if request.method == 'POST':
            data = request.POST
            name = data.get('name')
            price = data.get('price')
            description = data.get('description')
            stock = data.get('stock')
        
        Product.objects.create(
            name=name, 
            price=price, 
            description=description,
            stock=stock,
        )
        messages.auccess(request, "Producto creado")
    
    #esto corresponde al GET:
        return render ( 
            request,
            'prodcuts/create.html',
            {
                ""
            }
        )

# DEPRECADO
# def create_product(request): #!FALTA CREAR EL TEMPLATE
#     if request.method == 'POST':
#         data = request.POST
#         name = data.get('name')
#         price = data.get('price')
#         description = data.get('description')
#         stock = data.get('stock')
        
#         Product.objects.create(
#             name=name, 
#             price=price, 
#             description=description,
#             stock=stock,
#         )
#         messages.success(request, "Producto creado")
    
#     #esto corresponde al GET:
#     return render ( 
#         request,
#         'products/create.html',

#     )

class ProductCreate(CreateView):
    form_class = ProdcutForm # formulario a usar
    # model = Product
    template_name = 'products/create_from_class.html'
    success_url = reverse_lazy('product_list')
    # fields = ['name', 'price', 'description', 'stock'] # campos a mostrar en el formulario
    
    # def form_valid(self, form):
    #     messages.success(self.request, "Producto creado")
    #     return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['creador_producto'] = 'Crear producto' 
        return context
    
class OrderList (ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'
    
# DECRETADO    
# def order_list(request): #!PASARLO A VISTA BASADA EN CLASE
#     all_orders = OrderService.get_all()
#     return render(request, 
#             'orders/list.html',
#             {
#                 'orders': all_orders,
#             }
#             )
