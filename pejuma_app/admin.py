from django.contrib import admin
from .models import Job, Review

# Register your models here.
admin.site.register([Job, Review])