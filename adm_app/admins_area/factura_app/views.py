from django.shortcuts import render

# Create your views here.
def pitos(request):
    return render(request, "formulario.html", {})