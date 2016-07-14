from django.db import models
from django.contrib.auth.models import User
import os,shutil
from django.db.models.signals import pre_save
from django.db.models import signals
from redcross.settings import *

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	contact_number = models.CharField(max_length=10,null=True)
	address = models.CharField(max_length=200,null=True,blank=True)
	subscribe_to_newsletter = models.BooleanField(default=False)

	


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
