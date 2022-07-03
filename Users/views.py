from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.user.is_authenticated:
        return redirect('Videos:index')
    if request.method == 'POST':
        print('Login form is working')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:mian_page')
        else:
            return render(request, 'Users/login_page.html', {})
    return render(request, 'Users/login_page.html', {})

def logout_user(request):
    logout(request)
    return redirect('main:mian_page')