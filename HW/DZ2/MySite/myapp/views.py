from django.shortcuts import render


def home(request):
    return render(request, 'myapp/home.html')


def login_view(request):
    return render(request, 'myapp/login.html')


from django.shortcuts import render

# Create your views here.
