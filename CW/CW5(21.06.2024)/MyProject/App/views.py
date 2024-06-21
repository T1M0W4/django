from django.shortcuts import render
from .forms import Form


def login_view(request):
    return render(request, 'login.html')


def menu_view(request):
    return render(request, 'menu.html')

def get_form(request):
    form = Form()
    return render(request, 'login.html', {'form': form})