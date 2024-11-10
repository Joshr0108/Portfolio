from django.contrib import admin
from .models import CVFile
from .models import Skill

# Register your models here.

#Register CV File model
admin.site.register(CVFile)
admin.site.register(Skill)