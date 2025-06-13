# Create your views here.


from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage
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
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'), #se puede acceder asi: .get()
                email=form.cleaned_data['email'], #o asi [], porque es un diccionario
                password=form.cleaned_data['password1']
            )
        
            #envio de correo
            subject = "registro exitoso"
            message = render_to_string(
                'mails/welcome.html',
                {
                    'email': user.email
                }
            )
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[User.email]
            )
            email.content_subtype = "html" #para que lo inteprete como html
            email.send(
                fail_silently=False #si fallo no se manda
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