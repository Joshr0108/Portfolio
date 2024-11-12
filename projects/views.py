from django.shortcuts import render
from projects.models import Project
from pages.models import CVFile

def project_index(request):
    projects = Project.objects.all()
    cv = CVFile.objects.last()
    context = { #dictionary assigning projects to query
        "projects": projects,
        "cv": cv
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    cv = CVFile.objects.last()
    context = {
        "project": project,
        "cv": cv
    }
    return render(request, "projects/project_detail.html", context)