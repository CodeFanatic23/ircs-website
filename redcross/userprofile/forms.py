from django import forms
from .models import UserProfile
from PIL import Image
import os

class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField()

	address = forms.CharField(widget=forms.Textarea)
	widgets = {
	'message':forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].initial = self.instance.user.first_name
		self.fields['last_name'].initial = self.instance.user.last_name
		self.fields['email'].initial = self.instance.user.email

		


	def save(self, *args, **kwargs):
		super(UserProfileForm, self).save(*args, **kwargs)
		self.instance.user.first_name = self.cleaned_data.get('first_name')   
		self.instance.user.last_name = self.cleaned_data.get('last_name')
		self.instance.user.email = self.cleaned_data.get('email')
		self.instance.user.save()

	class Meta:
		model = UserProfile
		fields = ('first_name','last_name','contact_number','email','address','subscribe_to_newsletter')
	