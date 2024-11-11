from django.contrib import admin
from .models import CVFile
from .models import Skill, Learning

# Register your models here.

#Register CV File model
admin.site.register(CVFile)
admin.site.register(Skill)
admin.site.register(Learning)