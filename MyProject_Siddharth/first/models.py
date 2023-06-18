# Create your models here.
from django.db import models


class Book(models.Model):
    Auth_first_name = models.CharField(max_length=30)
    Auth_email = models.EmailField()
    Title = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Publication_Year = models.IntegerField(default=0)
    Issue_Status = models.BooleanField(default=False)
    Issued_Roll_No = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Book'

    def __str__(self):
        return self.Auth_first_name
