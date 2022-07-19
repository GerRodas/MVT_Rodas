from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from App_Familia.models import Miembro

# Create your views here.


def familiares(self, nombre, parentezco, edad, nacimiento):

    familiar= Miembro(nombre=nombre, parentezco=parentezco, edad=edad,nacimiento=nacimiento)
    familiar.save()
    return HttpResponse(f"""
    <h1>Agregué a {familiar.nombre}, mi {familiar.parentezco}, que tiene {familiar.edad} años</h1>
    """)

def lista_familiares(self):
    
    lista=Miembro.objects.all()

    return render(self, "template1.html", {"lista_familiares": lista})
