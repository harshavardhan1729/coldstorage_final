from django.contrib import admin

# Register your models here.
from .models import Coldstorage,Requests
admin.site.register(Coldstorage) 
admin.site.register(Requests)