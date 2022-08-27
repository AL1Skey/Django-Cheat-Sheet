from django.contrib import admin

# Register your models here.
from .models import Quest,Choice

#Registering models
admin.site.register(Quest)
admin.site.register(Choice)