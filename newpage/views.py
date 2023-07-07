from django.shortcuts import render

from .models import Usuario, tipoUsuario
# Create your views here.

def homepage(request):
    
    return render(request, "templates/homepage.html")

