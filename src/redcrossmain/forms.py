from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from multiupload.fields import MultiFileField
from .models import *

class PostForm(forms.ModelForm):
	CHOICES = (
        ('News', 'News'),
        ('Red-Cross-Stories', 'Red Cross Stories'),
        ('Disaster', 'Disaster'),
        ('Relief', 'Relief'),
        ('Community', 'Community'),
        # ('General', 'General'),
        ('Other','Other'),
    )
	CHOICES_STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )

	title = forms.CharField(required=True)
	content = forms.CharField(widget=CKEditorUploadingWidget())
	category = forms.ChoiceField(choices=CHOICES)
	status = forms.ChoiceField(choices=CHOICES_STATUS)


# class UploadForm(forms.ModelForm):
#     file = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)

#     class Meta:
#     	model = Attachment

#     	fields = ['file']

# class FileFieldForm(forms.Form):
#     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta:
#     	model = Attachment
#     	fields = ['file']

# class AlertForm(forms.Form):
# 	title = forms.CharField(required=True,widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))

# 	class Meta:
# 		model = Alert
# 		fields = ['title']

class BranchForm(forms.ModelForm):
	branches = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Here..'}))
	awards = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Here..'}))
	missions = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Here..'})) 
	something = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Here..'}))

	class Meta:
		model = Branch_Number
		fields = ['branches','awards','missions','something']



