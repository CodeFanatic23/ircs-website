from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

	address = forms.CharField(widget=forms.Textarea)
	widgets = {
	'message':forms.Textarea(attrs={'cols': 80, 'rows': 20}),}

	class Meta:
		model = UserProfile
		fields = ('first_name','last_name','contact_number','email','address')