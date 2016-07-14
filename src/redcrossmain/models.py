from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.mail.message import EmailMessage
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
import os
from django.core.mail import get_connection, EmailMultiAlternatives
from django.contrib.sites.models import Site
import patoolib
import re
import zipfile,os,shutil
import string, random
# Create your models here.

class Event(models.Model):
	event_name = models.CharField(max_length=40,blank=False,null=True)
	date = models.DateField(blank=False,null=True)
	description = models.CharField(max_length=300,blank=True,null=True)

class Post(models.Model):
	title  = models.CharField(max_length=100,blank=False,null=True)
	caption = models.CharField(max_length=300,blank=False,null=True)
	category = models.CharField(max_length=20,null=True,blank=True,default='Others')
	date = models.DateTimeField(auto_now_add=False,auto_now=True)
	content = RichTextUploadingField(config_name='default')
	preview_image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","posts","temporary"), blank=True,default=os.path.join(settings.MEDIA_ROOT,"uploads","posts","default.PNG"))
	status = models.CharField(max_length=10,null=True,blank=True,default='Draft')
	featured = models.BooleanField(default=False)
	title_slug = models.SlugField(editable=False)
	preview_image_name = models.CharField(max_length=150,blank=False,null=True,editable=False)
	link_to_post = models.URLField(null=True,blank=False,editable=False)

	def save(self, *args, **kwargs):
		self.title_slug = slugify(self.title)
		file_name = str(self.preview_image)
		file_name_cleaned = re.sub(' ', '_', file_name)
		self.preview_image_name = file_name_cleaned.split('/')[-1].lower()
		self.link_to_post = 'http://'+Site.objects.get_current().domain+'/posts/'+(self.category).lower()+'/'+(self.title_slug).lower()
		print(self.link_to_post)
		
		print(self.preview_image_name)

		super(Post, self).save(*args, **kwargs)


class Top_Slider(models.Model):
	images = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","temporary"),blank=False,null=True)
	remove_status = models.BooleanField(default=False)
	
	class Meta:
		verbose_name_plural = 'Change Homepage Slider Images'

class Team_Images(models.Model):
	images = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","temporary"),blank=False,null=True)
	date = models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name_plural = 'Change Our Team'

class Branch_Number(models.Model):
	branches = models.IntegerField(validators=[MinValueValidator(1)],blank=True,null=True)
	pmc = models.IntegerField(validators=[MinValueValidator(1)],blank=True,null=True,verbose_name='Primary Health Centres')
	bb = models.IntegerField(validators=[MinValueValidator(1)],blank=True,null=True,verbose_name='Blood Banks')
	members = models.IntegerField(validators=[MinValueValidator(1)],blank=True,null=True,verbose_name='Member count')

	class Meta:
		verbose_name_plural = 'Change Branch/PMC count '

	
class Alert(models.Model):
	title = models.CharField(max_length=255,null=True,blank=False)
	date = models.DateTimeField(auto_now_add=False,auto_now=True)
	image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","alerts"),null=True,blank=True)
	url = models.URLField(null=True,blank=True)

	class Meta:
		verbose_name_plural = 'Change Alerts'

class Newsletter(models.Model):
	title = models.CharField(max_length=50,null=True,blank=False)
	file = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","newsletter"))
	email_message = models.CharField(max_length=150,blank=True,null=True)
	date = models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name_plural = 'Newsletter'

class Rti(models.Model):
	rti = RichTextUploadingField()
	tenders = RichTextUploadingField()
	career = RichTextUploadingField()
	date = models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name_plural = "Change RTI/Tenders/Careers"
class Gallery(models.Model):
	album_name = models.CharField(max_length=20,null=True,blank=False)
	images = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"uploads","temporary"),blank=False,null=True)
	album_slug = models.SlugField(editable=False)

	def save(self, *args, **kwargs):
		self.title_slug = slugify(self.album_name)
		super(Gallery, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Gallery'


def upload(sender,instance,**kwargs):
	file_name = str(instance.images)
	file_name_cleaned = re.sub(' ', '_', file_name)

	try:
		print(instance.remove_status)
		if instance.remove_status == True:
			remove_dir(os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
			make_directory(os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
		uncompressFile(os.path.join(settings.MEDIA_ROOT,"uploads","temporary",file_name_cleaned),
			os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
		
		print("moving...")
		
		
		move(os.path.join(settings.MEDIA_ROOT,"uploads","topslider",str(file_name_cleaned.split("/")[-1]).split('.')[0]),
			os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
		remove_files(os.path.join(settings.MEDIA_ROOT,"uploads","temporary",file_name_cleaned))
		remove_dir(os.path.join(settings.MEDIA_ROOT,"uploads","topslider",str(file_name_cleaned.split("/")[-1]).split('.')[0]))
	except Exception as e:
		print(e)
		pass
signals.post_save.connect(upload,sender=Top_Slider)

def upload2(sender,instance,**kwargs):
	try:
		
		if instance.preview_image_name != 'default.png':
			make_directory(os.path.join(settings.MEDIA_ROOT,"uploads","posts",str(instance.category),str(instance.title_slug).lower()))
			move(os.path.join(settings.MEDIA_ROOT,"uploads","posts","temporary",instance.preview_image_name),
				os.path.join(settings.MEDIA_ROOT,"uploads","posts",str(instance.category),str(instance.title_slug).lower()))
		else:
			make_directory(os.path.join(settings.MEDIA_ROOT,"uploads","posts",str(instance.category),str(instance.title_slug).lower()))
			shutil.copy(os.path.join(settings.MEDIA_ROOT,"uploads","posts","default.png"),
				os.path.join(settings.MEDIA_ROOT,"uploads","posts",str(instance.category),str(instance.title_slug).lower()))
			print("Copied!")
	except Exception as e:
		print(e)
		pass
signals.post_save.connect(upload2,sender=Post)

def uploadGal(sender,instance,**kwargs):
	file_name = str(instance.images)
	file_name_cleaned = re.sub(' ', '_', file_name)
	file = file_name_cleaned.split('/')[-1].lower()
	print(file)
	
	
	try:
		make_directory(os.path.join(settings.MEDIA_ROOT,"uploads","gallery",str(instance.album_slug).lower()))	
		uncompressFile(os.path.join(settings.MEDIA_ROOT,"uploads","temporary",file),
			os.path.join(settings.MEDIA_ROOT,"uploads","gallery",str(instance.album_slug).lower()))	
		print("moving...")
		
		move(os.path.join(settings.MEDIA_ROOT,"uploads","gallery",str(instance.album_slug).lower(),file.split('.')[0]),
			os.path.join(settings.MEDIA_ROOT,"uploads","gallery",instance.album_slug))
		remove_files(os.path.join(settings.MEDIA_ROOT,"uploads","temporary",file))
		remove_dir(os.path.join(settings.MEDIA_ROOT,"uploads","gallery",str(instance.album_slug).lower(),file.split('.')[0]))
	except Exception as e:
		print(e)
		pass
signals.post_save.connect(uploadGal,sender=Gallery)


class Hometext(models.Model):

	slider_text_1 = models.CharField(max_length=50,blank=True,null=True)
	slider_text_2 = models.CharField(max_length=50,blank=True,null=True)
	slider_text_3 = models.CharField(max_length=50,blank=True,null=True)
	slider_text_4 = models.CharField(max_length=50,blank=True,null=True)
	slider_text_5 = models.CharField(max_length=50,blank=True,null=True)
	slider_read_more = models.CharField(max_length=100,blank=True,null=True)
	
	fmr_description = models.CharField(max_length=50,blank=True,null=True)
	bloodbank_description = models.CharField(max_length=50,blank=True,null=True)
	st_john_ambulance_description = models.CharField(max_length=50,blank=True,null=True)
	dm_description = models.CharField(max_length=50,blank=True,null=True)

	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name_plural = 'Home Page Text'

class Disease6m(models.Model):
	CHOICES_DISEASES = (
        (1, 'Unexplained Weight Loss'),
        (2, 'Ear piercing'),
        (3, 'Repeated Diarrhoea'),
        (4, 'Dental Extraction'),
        (5, 'Swollen Gland'),
        (6, 'Major Surgery'),
        (7,'Continuous Low-grade fever'),
        (8,'Minor Surgery'),
        (9,'Tatooing'),
        (10,'Blood Transfusion')
    )

	val = models.CharField(max_length=40,choices=CHOICES_DISEASES,blank=True,null=True)

class Taken24h(models.Model):
	CHOICES_EATEN = (
        ('antibiotics', 'Antibiotics'),
        ('steroids', 'Steroids'),
        ('aspirin', 'Aspirin'),
        ('vaccine', 'Vaccination'),
        ('alcohol', 'Alcohol'),
        ('dogbite', 'Dog Bite/Rabies Vaccine(1 year)'),
        ('bpmed','B.P. Medicine/Anti-depressant'),
    )
	val = models.CharField(max_length=40,choices=CHOICES_EATEN,blank=True,null=True)


class Suffered(models.Model):
	CHOICES_SUFFERED = (
        ('heartdisease', 'Heart Disease'),
        ('lungdisease', 'Lung Disease'),
        ('kidneydisease', 'Kidney Disease'),
        ('epilepsy', 'Epilepsy'),
        ('tb', 'Tuberculosis'),
        ('polycythemia','Polycythemia Vera'),
        ('leprosy','Leprosy'),
        ('hepatitis', 'Hepatitis B/C'),
        ('jaundice','Jaundice'),
        ('malaria','Malaria'),
        ('allergy','Allergic Disease'),
        ('diabetes','Diabetes'),
        ('asthma','Asthamactic Disease'),
        ('schizophrenia','Schizophrenia'),
        ('cancer','Cancer/Malignant Disease'),
        ('abnormalbleed','Abnormal Bleeding Tendency'),
        ('std','Sexually Transmitted Disease'),
        ('typhoid','Typhoid(Last 1 year)'),
        ('fainting','Fainting Spells'),
        ('hormonalimbal','Any Hormomal Imbalance'),
    )

	val = models.CharField(max_length=40,choices=CHOICES_SUFFERED,blank=True,null=True)

class Women(models.Model):
	CHOICES = (
        ('pregnant', 'Are you pregnant'),
        ('abortion_in_3_months', 'Have you had an abortion in the last three months'),
        ('childlessthan1yr', 'Do you have a child less than 1 year old'),
        ('childbreastfeed', 'Is the Child still breast feeding'),
        ('periods', 'Are you having your periods today'),
        )

	val = models.CharField(max_length=40,choices=CHOICES,blank=True,null=True)


class BloodDonation(models.Model):
	name = models.CharField(max_length=100,blank=False,null=True)
	date_of_birth = models.DateField(null=True,blank=False)
	nationality = models.CharField(max_length=50,blank=False,null=True)
	blood_group = models.CharField(max_length=50,blank=False,null=True)
	rh_factor = models.CharField(max_length=50,blank=False,null=True)
	father_name = models.CharField(max_length=100,blank=False,null=True)
	occupation = models.CharField(max_length=50,blank=False,null=True)
	organization = models.CharField(max_length=100,blank=False,null=True)
	address = models.CharField(max_length=400,blank=False,null=True)
	age = models.IntegerField(default=-1,blank=False)
	telephone_no = models.IntegerField(default=-1,blank=False)
	email = models.EmailField()
	mobile_number = models.IntegerField(default=-1,blank=False)
	weight = models.DecimalField(max_digits=5,decimal_places=2,default=0,null=True)
	height = models.CharField(max_length=7,blank=True,null=True)
	date = models.DateField(null=True,blank=True) 
	time = models.TimeField(null=True,blank=True)

	#questions
	accept_terms = models.BooleanField(default=False,blank=False)
	donated_blood_previously = models.BooleanField(default=False,blank=True)
	when_if_yes = models.CharField(max_length=30,blank=True,null=True)
	discomfort_during_donation = models.BooleanField(default=False,blank=True)
	eaten_in_last_24_hrs = models.BooleanField(default=False,blank=True)
	sleep_last_night = models.BooleanField(default=False,blank=True)
	acute_respiratory_problem = models.BooleanField(default=False,blank=True)
	reason_infected = models.BooleanField(default=False,blank=True)
	disease_last_6_months = models.ManyToManyField(Disease6m,blank=True)
	taken_following_in_last_24_hrs = models.ManyToManyField(Taken24h,blank=True)
	suffered_any_of_these = models.ManyToManyField(Suffered,blank=True)
	for_women = models.ManyToManyField(Women,blank=True)
	info_share = models.BooleanField(default=False,blank=False)
	terms_risks = models.BooleanField(default=False,blank=False)



def send_message(sender,instance,**kwargs):
	mail_list = []
	for i in User.objects.filter(userprofile__subscribe_to_newsletter=True):
			mail_list.append(i.email)
	
	print(mail_list[0])
	contact_message = render_to_string('newsletter2.0.html',{'title':instance.title,'message':instance.email_message})
	connection = get_connection() # uses SMTP server specified in settings.py
	connection.open()

	try:
		email = EmailMultiAlternatives(subject=str(instance.title), body=contact_message,from_email=settings.DEFAULT_FROM_EMAIL, to=mail_list, connection=connection)
		email.attach_alternative(contact_message, "text/html")
		email.sub_content_type = "html"
		email.attach_file(instance.file.path)
		email.send()
		connection.close()
		print("sent!")
	except Exception as e:
		print(e)
		pass

signals.post_save.connect(send_message,sender=Newsletter)




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
	if os.path.isdir(old):
		files = os.listdir(old)
		
		for f in files:
			shutil.move(os.path.join(old,f), new)
	else:
		shutil.move(old,new)
	    

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


