from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    auther = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(default = timezone.now)
    last_modified =  models.DateTimeField(auto_now = True)

class Section(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    book = models.ForeignKey(Book, related_name='sections', on_delete = models.CASCADE, default = None, null = True, blank = True)
    parent = models.ForeignKey('self', null = True, blank = True, on_delete = models.CASCADE, related_name= "subsection")
    user = models.ForeignKey(User, on_delete = models.CASCADE)
