from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from filer.fields.image import FilerImageField
# from filer.fields.file import FilerFileField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db.models import signals
import os
import patoolib
import re
import zipfile,os,shutil
# Create your models here.


	


class Post(models.Model):
	title  = models.CharField(max_length=100,blank=False,null=True)
	category = models.CharField(max_length=20,null=True,blank=True,default='O')
	date = models.DateTimeField(auto_now_add=False,auto_now=True)
	content = RichTextUploadingField(config_name='default')

# class Attachment(models.Model):
#     name = models.CharField(max_length=255,null=True)
#     logo = FilerImageField(null=True, blank=True,
#                            related_name="company_logo")
#     disclaimer = FilerFileField(null=True, blank=True,
#                                 related_name="company_disclaimer")

class Top_Slider(models.Model):
	images = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","temporary"),blank=False,null=True)
	remove_status = models.BooleanField(default=False)
	# date = models.DateTimeField(auto_now_add=False,auto_now=True)
	class Meta:
		verbose_name_plural = 'Change Homepage Slider Images'

class Team_Images(models.Model):
	images = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","temporary"),blank=False,null=True)
	date = models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name_plural = 'Change Our Team'

class Branch_Number(models.Model):
	branches = models.IntegerField(validators=[MinValueValidator(1)],blank=True,null=True)
	awards = models.IntegerField(validators=[MinValueValidator(1)],blank=True,null=True)
	missions = models.IntegerField(validators=[MinValueValidator(1)],blank=True,null=True)
	something = models.IntegerField(validators=[MinValueValidator(1)],blank=True,null=True)

	class Meta:
		verbose_name_plural = 'Change Branch/awards '

# class Alerts(models.Model):
# 	alert_1 = models.ForeignKey(Alert_Info,null=True)
	
class Alert(models.Model):
	title = models.CharField(max_length=255,null=True,blank=False)
	date = models.DateTimeField(auto_now_add=False,auto_now=True)
	image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","alerts"),null=True,blank=True)

	class Meta:
		verbose_name_plural = 'Change Alerts'

class Newsletter(models.Model):
	title = models.CharField(max_length=50,null=True,blank=False)
	file = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","newsletter"))
	date = models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name_plural = 'Home Page Text'

def upload(sender,instance,**kwargs):
	file_name = str(instance.images)
	file_name_cleaned = re.sub(' ', '_', file_name)

	try:
		# rename(os.path.join(settings.MEDIA_ROOT,"uploads","temporary",file_name_cleaned),
		# 	os.path.join(settings.MEDIA_ROOT,"uploads","temporary","images.zip"))
		print(instance.remove_status)
		if instance.remove_status == True:
			remove_dir(os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
			make_directory(os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
		uncompressFile(os.path.join(settings.MEDIA_ROOT,"uploads","temporary",file_name_cleaned),
			os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
		
		print("moving...")
		
		
		move(os.path.join(settings.MEDIA_ROOT,"uploads","topslider",str(file_name_cleaned.split('/')[-1]).split('.')[0]),
			os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
		remove_files(os.path.join(settings.MEDIA_ROOT,"uploads","temporary",file_name_cleaned))
		remove_dir(os.path.join(settings.MEDIA_ROOT,"uploads","topslider",str(file_name_cleaned.split('/')[-1]).split('.')[0]))
	except Exception as e:
		print(e)
		pass
signals.post_save.connect(upload,sender=Top_Slider)

# def upload_clean(sender,instance,**kwargs):
# 	try:
# 		print(instance.remove_status)
		
# 			remove_dir(os.path.join(settings.MEDIA_ROOT,"uploads","temporary"))
# 			make_directory(os.path.join(settings.MEDIA_ROOT,"uploads","temporary"))
# 		else:
# 			pass
# 	except Exception as e:
# 		print(e)
# 		pass
# signals.pre_save.connect(upload,sender=Top_Slider)

class Hometext(models.Model):

	slider_text_1 = models.CharField(max_length=50,blank=True,null=True)
	slider_text_2 = models.CharField(max_length=50,blank=True,null=True)
	slider_text_3 = models.CharField(max_length=50,blank=True,null=True)
	slider_text_4 = models.CharField(max_length=50,blank=True,null=True)
	
	fmr_description = models.CharField(max_length=50,blank=True,null=True)
	bloodbank_description = models.CharField(max_length=50,blank=True,null=True)
	st_john_ambulance_description = models.CharField(max_length=50,blank=True,null=True)
	dm_description = models.CharField(max_length=50,blank=True,null=True)

	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name_plural = 'Home Page Text'


def uncompressFile(from_location,to_location):
	if from_location.endswith(".zip"):
		zfile = zipfile.ZipFile(from_location)
		zfile.extractall(to_location)
		print("uncompressing:" + from_location) 	

	elif from_location.endswith(".rar"):
		patoolib.extract_archive(from_location, outdir=to_location) 

def remove_files(location):
	os.remove(location)
	print("deleting:" + location)

def remove_dir(location):
	shutil.rmtree(location)
	print("deleting:" + location)

def move(old,new):
	files = os.listdir(old)
	
	for f in files:
		shutil.move(os.path.join(old,f), new)
	    

def rename(old,new):
	os.rename(old,new)
	print("renaming:"+old+"to:"+new)

def make_directory(location):
		#making desired directory if not present
		try:
			os.makedirs(location)
			print("making" + location)
		#PENDING WORK: user might enter the same event_name so we need to keep a check.That work is not done, we need to keep a check here.
		except OSError:
			if not os.path.isdir(location):
				raise