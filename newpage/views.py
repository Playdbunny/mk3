from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

from .forms import UsuarioForm, tipoForm
from .models import Usuario, tipoUsuario
# Create your views here.

def homepage(request):
    index = open("D:/Fernanda/Documents/mk3/newPage/templates/homepage.html")
    template = Template(index.read())
    index.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def bandanas(request):
    bandana = open("D:/Fernanda/Documents/mk3/newPage/templates/bandana.html")
    template = Template(bandana.read())
    bandana.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def crud(request):
    usuarios = Usuario.objects.all()
    context = {"usuario" : UsuarioForm}
    return render(request, 'templates/user_list.html', context)
