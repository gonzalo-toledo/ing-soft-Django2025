from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django .urls import reverse_lazy
from django.views import (
    View,  # no tienen tanto poder como views.generic. Mas enfocado a vistas de funciones
)
from django.views.generic import CreateView, DeleteView, DetailView, ListView


from products.forms import  CustomerForm, OrderDetailForm, OrderForm, ProductForm
from products.models import Customer, Order, Product, OrderDetail

# Create your views here. 

# CLIENTES
class CustomerCreate(CreateView):
    form_class = CustomerForm
    template_name = 'customers/create.html'
    success_url = reverse_lazy('customer_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creador_cliente'] = 'Crear cliente'
        return context
    
class CustomerList(ListView):
    model = Customer # modelo a usar
    template_name = 'customers/list.html' # template a usar en la vista
    context_object_name = 'customers' # nombre del contexto a usar en el template

class CustomerDetail(DetailView):
    model = Customer 
    template_name = 'customers/detail.html' 
    context_object_name = 'customer'
    pk_url_kwarg = 'customer_id' # nombre con el que va a buscar el ID en la url

class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customers/delete.html'
    content_object_name = 'customer'
    pk_url_kwarg = 'customer_id'
    success_url = reverse_lazy('customer_list') # redirecciona a la lista de clientes. 'customer_list' es el name de la url

    
# PRODUCTOS
class ProductList (ListView):
    model = Product # modelo a usar
    template_name = 'products/list.html' # template a usar en la vista
    context_object_name = 'products' # nombre del contexto a usar en el template

class ProductDetail (DetailView):
    model = Product 
    template_name = 'products/detail.html' 
    context_object_name = 'product'
    pk_url_kwarg = 'product_id' # nombre con el que va a buscar el ID en la url
    
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
        messages.success(request, "Producto creado")
        return redirect('product_list')
    #esto corresponde al GET:
        # return render ( 
        #     request,
        #     'products/create.html',
        # )

class ProductCreate(CreateView):
    form_class = ProductForm # formulario a usar
    #model = Product
    template_name = 'products/create_from_class.html'
    success_url = reverse_lazy('product_list')
    # fields = ['name', 'price', 'description', 'stock'] # campos a mostrar en el formulario
    
    # def form_valid(self, form):   #sirve para validar el formulario
    #     messages.success(self.request, "Producto creado")
    #     return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['creador_producto'] = 'Crear producto' 
        return context
    
    
# ORDENES
class OrderList (ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'
    
class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/create.html'
    success_url = reverse_lazy('order_create')
    
    
class OrderDetailCreate(CreateView):
    model = Order
    form_class = OrderDetailForm
    template_name = 'orders_detail/create.html'
    success_url = None
    
    def get_initial(self):
        #devuevle un diccionario con los valores iniciales para el formulario
        order_id = self.kwargs.get('order_id')
        return {'order': order_id} #order es el atributo de OrderDetailForm
    
    def get_success_url(self):
        #Esto hace que se quede en la misma página luego del exito de la llamada
        return reverse_lazy(
            'order_detail', 
            kwargs={
                'order_id':self.kwargs.get('order_id')
            })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # order = Order.objects.get(id=self.kwargs.get('order_id')) #?se puede hacer así ó con get_object_or_404
        order = get_object_or_404(Order, id=self.kwargs.get('order_id'))
        details = order.details.all() #en el moldeo de OrderDetail se usa related_name = "details". Es lomismo que hacer: details = OrderDetail.objects.filter(order=order)
        context ['order'] = order
        details = [
            {
                'product': detail.product,
                'quantity': detail.quantity,
                'subtotal': detail.product.price * detail.quantity,
            }
            
            for detail in details
        ]
        context ['details'] = details
        context ['total'] = sum(detail['subtotal'] for detail in details)
        return context