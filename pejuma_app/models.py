from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    artisan = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)