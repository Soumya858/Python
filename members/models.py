from django.db import models

class form(models.Model):
  fname = models.CharField(max_length=55)
  lname = models.CharField(max_length=55)
  age=models.IntegerField()
  email=models.CharField(max_length=70)
  class meta:
    db_table='form'