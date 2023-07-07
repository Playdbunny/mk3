from django.shortcuts import render

from .models import Usuario, tipoUsuario
# Create your views here.

def homepage(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "pages/homepage.html", context)

