from django.shortcuts import render

# Create your views here.

def get_index(request):
    return render(request, "index.html")

def contacts(request):
    return render(request, "contact.html")
