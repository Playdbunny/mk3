#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("bandanas/", views.bandanas, name="bandanas"),
    path('crud', views.crud, name='crud'),
]
