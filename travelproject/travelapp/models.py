from django.db import models

# Create your models here.
class place(models.Model):
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=200)
    desc=models.TextField()
    def __str__(self):
        return self.name