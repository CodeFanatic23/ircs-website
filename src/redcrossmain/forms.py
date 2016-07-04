from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class PostForm(forms.ModelForm):
	title = forms.CharField(required=True)
	content = forms.CharField(widget=CKEditorUploadingWidget())

	class Meta:
		model = Post
		fields = ['title','content']