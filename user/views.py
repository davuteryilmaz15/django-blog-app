from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib  import messages
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        dj_login(request, newUser)
        messages.success(request, 'Başarıyla kayıt oldunuz.')

        return redirect('index')
    else:
        context = {
            "form" : form
        }
        return render(request, 'register.html', context)
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            
            return redirect('index')
        else:
            context = {
                "form" : form
            }
            return render(request, 'register.html', context)
    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request, 'register.html', context)
    """

def login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Kullanıcı adı veya parola hatalı.')
            return render(request, 'login.html', context)
        
        dj_login(request, user)
        messages.success(request, 'Giriş Başarılı.')
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('article:dashboard')

    return render(request, 'login.html', context)

def logout(request):
    dj_logout(request)
    messages.success(request, 'Çıkış Başarılı.')
    return redirect('index')