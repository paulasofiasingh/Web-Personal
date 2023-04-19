from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request): # Recibe un parámetro request, que es la petición de que se quiere ver la portada de nuestra página
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})