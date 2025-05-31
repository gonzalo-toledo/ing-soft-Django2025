from django import forms

from products.models import Customer, Product 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock', 'image']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio del producto',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del producto',
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Stock del producto',
                }
            ),
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del cliente',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo del cliente',
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }