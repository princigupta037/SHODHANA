from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)


