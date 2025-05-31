from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.views import View
from home.forms import RegisterForm, LoginForm

    
class HomeView(View):
    def get(self, request):
        return render(
            request,
            'index.html',
        )
    
class RegisterView(View):
    def get (self, request):
        form = RegisterForm()
        return render(
            request,
            'account/register.html',
            {
                'form': form
            }
        )
    def post (self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('username'), #se puede acceder asi: .get()
                email=form.cleaned_data['email'], #o asi [], porque es un diccionario
                password=form.cleaned_data['password1']
            )
            messages.success(request, "Usuario creado correctamente") 
        
        return render(
            request,
            'account/register.html',
            {
                'form': form
            }
        )        
        


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            'account/login.html',
            {
                "form": form
            }
        )
    def post (self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(  #authtenticate verifica si el usuario existe pero no lo loguea
                request, 
                username=username, 
                password=password
            )
            
            if user is not None: #se usa None porque si no existe el usuario devuelve None
                login(request, user) #loguea al usuario
                return redirect('../products/product_list') #redirecciona a la vista de productos
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
                
        return render(request, 
            "account/login.html", 
            {"form": form}) 

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')