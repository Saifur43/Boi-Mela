from django.shortcuts import render

def home(request):
    return render(request, 'bookinfo/home.html')
