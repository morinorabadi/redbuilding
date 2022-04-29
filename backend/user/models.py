from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    firsname = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)

    lastname = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)


class MoriToken(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50)
