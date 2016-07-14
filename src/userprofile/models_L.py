from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=70,null=True)
	last_name = models.CharField(max_length=50,null=True)
	contact_number = models.CharField(max_length=10,null=True)
	email = models.EmailField(blank=True,null=True)
	address = models.CharField(max_length=200,null=True,blank=True)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])