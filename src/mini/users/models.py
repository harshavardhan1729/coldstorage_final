from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)
# Create your models here.
# from django import models,migrations
# class Migration(migrations.Migration):
#     depend
class UserManager(BaseUserManager):
    def create_user(self,email,full_name,password=None,is_active=True):
        if not email:
            raise ValueError("Users must have email ")
        if not full_name:
            raise ValueError("Users must have full name")
        if not password:
            raise ValueError("users must have password")
        user_obj=self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password)
        user_obj.active=is_active
        user_obj.save(using=self._db)
        return user_obj
    def create_superuser(self,email,full_name,password=None):
        user=self.create_user(
            email,
            full_name=full_name,
            password=password,
    
            is_active=True
        )
        return user


class User(AbstractBaseUser):
    email=models.EmailField(max_length=255,unique=True)
    active=models.BooleanField(default=True)
    staff=models.BooleanField
    full_name=models.CharField(max_length=255,blank=True,null=False)#
    timestamp=models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name']
    
    objects=UserManager()
    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    @property
    def is_active(self):
        return self.active
    def is_staff(self):
        return self.staff
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True


class GuestEmail(models.Model):
    email=models.EmailField()
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email