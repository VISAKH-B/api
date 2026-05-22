from django.db import models
class tbl_todo(models.Model):
    text=models.CharField(max_length=200)
    date=models.DateField()
# Create your models here.
