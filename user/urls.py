from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('register/', views.register, name = 'userRegister'),
    path('login/', views.login, name = 'userLogin'),
    path('logout/', views.logout, name = 'userLogout'),
]