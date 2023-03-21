from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Commande(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    votre_cmd = models.CharField(max_length=100)
    cmd_supp = models.CharField(max_length=100)
    decert = models.CharField(max_length=100)
    delivery_date = models.DateTimeField()
    nb_cmd = models.IntegerField(blank=True, null=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    # date_commanded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    