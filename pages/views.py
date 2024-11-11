from django.shortcuts import render
from .models import CVFile
from .models import Skill, Learning

# Create your views here.

def home(request):
    cv = CVFile.objects.last() # get latest CV
    return render(request, "pages/home.html", {'cv': cv})

def skill_learning_view(request):
    print("Skills view is being called")  # Debugging
    skills = Skill.objects.all()
    learnings = Learning.objects.all()
    return render(request, 'pages/home.html', {'skills': skills, 'learnings': learnings})