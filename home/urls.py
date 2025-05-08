from django.urls import path

from home.views import  home, login_view, logout_view , register 


urlpatterns = [
    path(route='register/', 
        view=register, 
        name='register',
    ),
    path(route='login/',
        view=login_view, 
        name='login',
    ),   
    path(route='logout/',
        view=logout_view, 
        name='logout',
    ),
    path(route='',
        view=home, 
        name='index',
    ),
]