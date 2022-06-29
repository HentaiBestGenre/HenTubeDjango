from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='Users:login')
def Index(request):
    return render(request, 'Videos/index.html', {})

@login_required(redirect_field_name='Videos:index2', login_url='Users:login')
def Index2(request):
    return render(request, 'Videos/index2.html', {})
