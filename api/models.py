from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from datetime import date
import datetime
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    birthday = models.DateField(default=datetime.date.today)
    cellphone = models.IntegerField(blank=False, null=False, default=2222222222)
    parentID = models.ForeignKey('auth.User', related_name='sons', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class Schedule(models.Model):
    name = models.CharField(max_length=50, blank=False)
    sonID = models.ForeignKey('Son', related_name='schedules', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class Activity(models.Model):
    name = models.CharField(max_length=50   , blank=False)
    description = models.CharField(max_length=200, blank=False)
    steps = models.CharField(max_length=500, blank=False)
    imagePath = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(blank=False)
    duration = models.IntegerField(blank=False, null=False, default=0)
    scheduleID = models.ForeignKey('Schedule', related_name='activities', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class PanicButtonCall(models.Model):
    activityID = models.ForeignKey('Activity', on_delete=models.CASCADE)
    sonID = models.ForeignKey('Son', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


# This receiver handles token creation when a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
