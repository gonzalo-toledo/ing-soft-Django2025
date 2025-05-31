from django.urls import path


from products.views import ProductList, ProductDetail, ProductDelete, OrderList, ProductCreate, CustomerCreate, CustomerList, CustomerDetail, CustomerDelete


urlpatterns = [
    # CLIENTES
    path(route='customer_create/', 
        view=CustomerCreate.as_view(), 
        name='customer_create'
    ),
    
    path(route='customer_detail/<customer_id>/',
    view=CustomerDetail.as_view(), 
        name='customer_detail'
    ),
    path(route='customer_delete/<customer_id>/',
        view=CustomerDelete.as_view(), 
        name='customer_delete'
    ),
    
    path(route='customer_list/', 
        view= CustomerList.as_view(), 
        name='customer_list'
    ),
    
    # PRODUCTOS
    path(route='product_create/', 
        view=ProductCreate.as_view(), 
        name='product_create'
    ),
    
    path(route='product_detail/<product_id>/',
    view=ProductDetail.as_view(), 
        name='product_detail'
    ),
    path(route='product_delete/<product_id>/',
        view=ProductDelete.as_view(), 
        name='product_delete'
    ),
    
    path(route='product_list/', 
        view= ProductList.as_view(), 
        name='product_list'
    ),
    
    
    # ORDENES
    path(route='order_list/', 
        view=OrderList.as_view(), 
        name='order_list',
    ),
    
]
