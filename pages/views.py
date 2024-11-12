from django.shortcuts import render
from .models import CVFile
from .models import Skill, Learning

# Create your views here.


def home(request): 
    skills = Skill.objects.all()
    learnings = Learning.objects.all()
    cv = CVFile.objects.last()
    return render(request, 'pages/home.html', {'skills': skills, 'learnings': learnings, 'cv':cv })