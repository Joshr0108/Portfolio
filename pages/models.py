from django.db import models

# Create your models here.

# Create model for updatable CV file
class CVFile(models.Model):
    file = models.FileField(upload_to='cv/')
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CV uploaded on  {self.upload_at}"

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Learning(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description
    
