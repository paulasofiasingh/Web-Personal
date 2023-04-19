from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request): # Recibe un parámetro request, que es la petición de que se quiere ver la portada de nuestra página
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')