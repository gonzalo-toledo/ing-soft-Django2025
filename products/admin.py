from django.contrib import admin

# Register your models here.
from products.models import Customer, Order, OrderDetail, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'stock', 'image')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'customer')
    

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    