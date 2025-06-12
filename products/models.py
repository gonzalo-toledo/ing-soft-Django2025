from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description= models.TextField()
    stock= models.IntegerField()
    image= models.ImageField(upload_to='products/', null=True, blank=True)  
    
    def __str__(self):
        return self.name
    

#cliente
class Customer(models.Model): 
    name= models.CharField(max_length=255)
    email= models.EmailField()
    phone= models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


#orden de compra 
class Order(models.Model):
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE,
        )
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Orden n° {self.id} del cliente: {self.customer.name}"


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE,
        related_name="details", #para acceder a los detalles de la orden
        )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        )
    quantity = models.IntegerField()
    history = HistoricalRecords()
    
    def __str__(self):
        # return f"{self.quantity} x {self.product}"
        return str(self.pk)
    

class OrderDetailAuditLog(models.Model):
    """
    Modelo para registrar los cambios de OrderDetail
    """
    order_detail = models.ForeignKey(
        OrderDetail, 
        on_delete=models.CASCADE,
        related_name = "details"
        )
    actions = models.CharField(
        max_length=100,
        choices=[
            ('created', 'Creado'),
            ('updated', 'Actualizado'),
        ]
        )
    quantity = models.IntegerField()
    product_name = models.CharField(
        max_length=255
        )
    timestamp = models.DateTimeField(
        auto_now_add=True
        )