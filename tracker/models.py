from django.db import models

# Create your models here.

class input(models.Model):
    link = models.URLField(max_length=500)
    price = models.FloatField()
    email = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.email