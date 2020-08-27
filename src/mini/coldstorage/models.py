from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# from phone_field import PhoneField

# class displayusername(models.Model):
#     username=models.CharField(max_length=100)


class Coldstorage(models.Model):
    name=models.CharField(max_length=155,blank=None)
    
    description=models.TextField()
    phone = models.CharField(max_length=12)
    total_storage=models.IntegerField()
    storage_left=models.IntegerField()
    date_modified=models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.EmailField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coldstorage-detail',kwargs={'pk':self.pk})
