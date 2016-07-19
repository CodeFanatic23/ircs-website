from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from .forms import UserProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST,instance = request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		user = request.user
		profile = user.profile
		form = UserProfileForm(instance=profile)
	context = {
	'form':form,
	}

	return render(request,'profile.html',context)


