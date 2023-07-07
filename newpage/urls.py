#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("bandanas/", views.bandanas, name="bandanas"),
    path("correas/", views.correas, name="correas"),
    path("identificaciones/", views.identificaciones, name="identificaciones"),
    path("about/", views.about, name="about"),
    path('crud', views.crud, name='crud'),
]
