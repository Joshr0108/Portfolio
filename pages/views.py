from django.shortcuts import render
from .models import CVFile

# Create your views here.

def home(request):
    cv = CVFile.objects.last() # get latest CV
    return render(request, "pages/home.html", {'cv': cv})