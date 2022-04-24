from django.db import models


class BossUser(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    firsname = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)

    lastname = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)


class WorkerUser(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    boss = models.ForeignKey(BossUser, on_delete=models.CASCADE)

    firsname = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)

    lastname = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)


class MoriToken(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=True)
    user_id = models.IntegerField()
    is_boss = models.BooleanField(default=True)
    token = models.CharField(max_length=50)

