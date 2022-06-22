from cgitb import text
from distutils import text_file
from sqlite3 import Timestamp
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, DateTimeField
from django.contrib.auth import get_user_model

# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Timestamp =  models.DateTimeField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name="Blogpost")
    
