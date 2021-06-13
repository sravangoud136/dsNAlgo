from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Tag(models.Model):
    tag=models.CharField(max_length=100)
    def __str__(self):
        return self.tag

class Problem(models.Model):
    problem_id=models.IntegerField(primary_key=True,default=1)
    Description=models.CharField(max_length=1000)
    Code=models.TextField()
    Language=models.CharField(max_length=20,default=None)
    tag=models.ForeignKey('Tag',on_delete=models.CASCADE)
    def __str__(self):
        return self.Description

    
