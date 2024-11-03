from django.db import models

# Create your models here.

# Create model for updatable CV file
class CVFile(models.Model):
    file = models.FileField(upload_to='cv/')
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CV uploaded on  {self.upload_at}"
