from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False)
    lastName = models.CharField(max_length=20, blank=False)
    cellphone = models.IntegerField(blank=False, null=False, default=2222222222)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class Son(models.Model):
    name = models.CharField(max_length=20, blank=False)
    lastName = models.CharField(max_length=20, blank=False)
    code = models.CharField(max_length=8, blank=False)
    gender = models.CharField(max_length=8, blank=False)
    cellphone = models.IntegerField(blank=False, null=False, default=2222222222)
    parentID = models.ForeignKey('auth.User', related_name='sons', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

# This receiver handles token creation when a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
