from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

from .forms import UsuarioForm, tipoForm
from .models import Usuario, tipoUsuario
# Create your views here.

def homepage(request):
    index = open("C:/Users/CETECOM/Desktop/mk3/newPage/templates/homepage.html")
    template = Template(index.read())
    index.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def bandanas(request):
    bandana = open("C:/Users/CETECOM/Desktop/mk3/newPage/templates/bandanas.html")
    template = Template(bandana.read())
    bandana.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def correas(request):
    correa = open("C:/Users/CETECOM/Desktop/mk3/newPage/templates/correas.html")
    template = Template(correa.read())
    correa.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def identificaciones(request):
    identificacion = open("C:/Users/CETECOM/Desktop/mk3/newPage/templates/identificaciones.html")
    template = Template(identificacion.read())
    identificacion.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def about(request):
    about = open("C:/Users/CETECOM/Desktop/mk3/newPage/templates/sobrenosotros.html")
    template = Template(about.read())
    about.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def crud(request):
    usuarios = Usuario.objects.all()
    context = {"usuario" : UsuarioForm}
    return render(request, 'templates/user_list.html', context)
