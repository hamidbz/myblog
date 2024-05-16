from django.db import models



class MesageModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mesg = models.TextField()