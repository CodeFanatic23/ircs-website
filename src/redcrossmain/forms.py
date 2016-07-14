from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class PostForm(forms.ModelForm):
	CHOICES = (
        ('news', 'News'),
        ('red-cross-stories', 'Red Cross Stories'),
        ('disaster', 'Disaster'),
        ('relief', 'Relief'),
        ('community', 'Community'),
        ('alerts', 'Alerts'),
        ('other','Other'),
    )
	CHOICES_STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )

	title = forms.CharField(required=True)
	content = forms.CharField(widget=CKEditorUploadingWidget())
	category = forms.ChoiceField(choices=CHOICES)
	status = forms.ChoiceField(choices=CHOICES_STATUS)



class BranchForm(forms.ModelForm):
	branches = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Here..'}))
	pmc = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Here..'}))
	bb = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Here..'})) 
	members = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Here..'}))

	class Meta:
		model = Branch_Number
		fields = '__all__'


class BloodDonationForm(forms.ModelForm):	
	# name = forms.CharField(widget=forms.TextInput,required=True)
	# date_of_birth = forms.CharField(widget=forms.DateInput,required=True)
	# nationality = forms.CharField()
	# blood_group = forms.CharField()
	# rh_factor = forms.CharField(required=False)
	# father_name = forms.CharField(required=False)
	# occupation = forms.CharField(required=False)
	# organization = forms.CharField(required=False)
	# address = forms.CharField(widget=forms.Textarea(attrs={'rows':10,'col':40}))
	# age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
	# telephone_no = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
	# email = forms.EmailField(required=False)
	# mobile_number = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
	# weight = forms.CharField(required=False)
	# height = forms.CharField(required=False)
	# date = forms.DateTimeField(widget=forms.DateInput,required=False)
	# time = forms.DateTimeField(widget=forms.TimeInput,required=False)
	
	# #questions
	# accept_terms = forms.BooleanField(required=True)
	# donated_blood_previously = forms.BooleanField(required=True)
	# if_yes_when = forms.CharField(widget=forms.TextInput,required=False)
	# discomfort_during_donation = forms.BooleanField(required=True)
	# eaten_in_last_24_hrs = forms.BooleanField(required=False)
	# sleep_last_night = forms.BooleanField(required=False)
	# acute_respiratory_problem = forms.BooleanField(required=False)
	# reason_infected = forms.BooleanField(required=False)
	# disease_last_6_months = forms.ModelMultipleChoiceField(queryset=Disease6m.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
	# taken_following_in_last_24_hrs = forms.ModelMultipleChoiceField(queryset=Taken24h.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
	# suffered_any_of_these = forms.ModelMultipleChoiceField(queryset=Suffered.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
	# for_women = forms.ModelMultipleChoiceField(queryset=Suffered.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
	# info_share = forms.BooleanField(required=False)
	# terms_risks = forms.BooleanField(required=False)

	class Meta:
		model = BloodDonation
		fields = '__all__'
	def __init__(self,*args,**kwargs):
		super(BloodDonationForm, self).__init__(*args, **kwargs)
		self.fields['disease_last_6_months'].choices = Disease6m.CHOICES_DISEASES
		self.fields['taken_following_in_last_24_hrs'].choices = Taken24h.CHOICES_EATEN
		self.fields['suffered_any_of_these'].choices = Suffered.CHOICES_SUFFERED
		self.fields['for_women'].choices = Women.CHOICES
		self.fields['for_women'].label = "FOR WOMEN DONORS"
		self.fields['info_share'].label = "Would you like to be informed about any abnormal test result at the address furnished by you?"
		self.fields['terms_risks'].label = "Have you read and understood all the information presented and answered all the questions truthfully, as any incorrect statement may affect your health or the recipient"


	



