from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

from .models import Usuario, tipoUsuario
# Create your views here.

def homepage(request):
    index = open("D:/Fernanda/Documents/mk3/newPage/templates/homepage.html")
    template = Template(index.read())
    index.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

