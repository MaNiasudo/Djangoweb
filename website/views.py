from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Welcome Home")

def about_view(request):
    return HttpResponse("About the website")

def contact_view(request):
    return HttpResponse("<h1>Contacts</h1>")
