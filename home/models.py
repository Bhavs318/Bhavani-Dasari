from django.db import models

# Create your models here.
class Library(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    ISBN= models.CharField(max_length=5, unique=True)
   Publication_year=models.CharField(max_length=5,Unique=true)
    Genre = models.CharField(max_length=10)

    def _str_(self):
        return self.Title + ' ' + self.Author