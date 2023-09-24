from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def help(request):
    return HttpResponse("Help is here")

def about(request):
    return HttpResponse("There is gonna be information about company")

def contact(request):
    return HttpResponse("Contact numbers are gonna be here")