from django.shortcuts import render

from .models import Usuario, tipoUsuario
# Create your views here.

def homepage(request):
    context = {}
    return render(request, "templates/homepage.html", context)

