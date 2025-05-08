from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(
        request,
        'index.html',
    )

def register(request):
    if request.method == 'POST':        
        data = request.POST
        username = data.get('username')
        pass1 = data.get('password1')
        pass2 = data.get('password2')
        email = data.get('email')
        print(username, pass1, pass2)
        
        if not username or not pass1 or not pass2:
            raise "no hay data" #no seria necesario ya que el formulario tiene required
        elif pass1 != pass2:
            messages.error(request, "las contraseñas no son iguales")
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
        else:
            User.objects.create_user(
                username=username, 
                email=email, 
                password=pass1
            )
            print("Usuario creado")    
    
    return render(
        request,
        'account/register.html',
        {

        }
    )

def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(  #authtenticate verifica si el usuario existe pero no lo loguea
            request, 
            username=username, 
            password=password)
        if user is not None: #se usa None porque si no existe el usuario devuelve None
            login(request, user) #loguea al usuario
            return redirect('../products/product_list') #redirecciona a la vista de productos
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            
        
    return render(request, "account/login.html") 

def logout_view(request):
    logout(request) #desloguea al usuario
    return redirect('index') #redirecciona a la vista de index

def _validate_pass(pass1, pass2):
    pass1 == pass2
