from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Post(models.Model):
	title  = models.CharField(max_length=100,blank=False,null=True)
	date = models.DateTimeField(auto_now_add=False,auto_now=True)
	content = RichTextUploadingField(config_name='default')