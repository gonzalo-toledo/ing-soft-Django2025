from django.urls import path

from products.views import customer_list
# create_product
from products.views import ProductList, ProductDetail, ProductDelete, OrderList, ProductCreate
#,ProductCreateView 

urlpatterns = [
    path(route='order_list/', 
        view=OrderList.as_view(), # cambiamos a vista basada en clase
        name='order_list',
    ),
    
    path(route='product_create/', 
        view=ProductCreate.as_view(), # cambiamos a vista basada en clase
        name='product_create'
    ),
    
    path(route='product_detail/<product_id>/',
    view=ProductDetail.as_view(), # cambiamos a vista basada en clase
        name='product_detail'
    ),
    path(route='product_delete/<product_id>/',
        view=ProductDelete.as_view(), # cambiamos a vista basada en clase
        name='product_delete'
    ),
    
    path(route='product_list/', 
        view= ProductList.as_view(), # cambiamos a vista basada en clase
        name='product_list'
    ),
    
    path(route='customer_list/',
        view=customer_list,
        name='customer_list'
    ),
    
]
