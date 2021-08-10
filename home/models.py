from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class TaskModel(models.Model):
    judul=models.CharField(max_length=50)
    waktu=models.DateTimeField()
    pengguna=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
	    return "{}.{}".format(self.judul,self.pengguna)