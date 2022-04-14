
from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=100 )
    body=models.TextField()
    phone = models.IntegerField()
    img=models.ImageField(upload_to='img/project/%y/%m/%d')
    creat_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def GetUrl(self):
        return reverse('detiles',args=[self.id])