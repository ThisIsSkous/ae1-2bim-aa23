from django.shortcuts import render
from invetario.models import EntidadInventario

# Create your views here.
def bodegas(request):
    mis_bodegas = EntidadInventario.objects.all()
    informacion_template = {"mis_entidades":mis_bodegas}
    return render(request, "bodegas.html", informacion_template)


