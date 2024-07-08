from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=55, blank=False)
  email = models.EmailField( blank=False)
  roll = models.IntegerField( blank=False)

  