

from django.db import models
import urlparse
class Names(models.Model):
    name = models.CharField(max_length=500)
   # address = models.CharField(max_length=250)
   # phone = models.CharField(max_length=250)
    link = models.CharField(max_length=500, null= True)
    results = models.CharField(max_length=500)

    def __str__(self):
        return self.link

class Character(models.Model):
    namelink = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.namelink