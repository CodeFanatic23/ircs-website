from django.shortcuts import render
from django.conf import settings
# from django.core.urlresolvers import reverse_lazy
# from django.views.generic import ListView
# from django.views.generic.edit import CreateView
# from mutant import models	
from django.http import HttpResponse
from .models import *
from .forms import *
import re

# Create your views here.
def home(request):
	alertobj = Alert.objects.all()
	sliderobj = os.listdir(os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
	slimg = []
	for a in sliderobj:
		slimg.append(a)
	alert = []
	image = []
	for i in alertobj:
		alert.append(i.title)
		image.append(str(i.image).split('/')[-1])

	nosobj = Branch_Number.objects.all()

	hometxtobj = Hometext.objects.all()
	for d in hometxtobj:
		slider_text_1 = d.slider_text_1
		slider_text_2 = d.slider_text_2
		slider_text_3 = d.slider_text_3
		slider_text_4 = d.slider_text_4

		fmr_description = d.fmr_description
		dm_description = d.dm_description
		st_john_description = d.st_john_ambulance_description
		bloodbank_description = d.bloodbank_description




	print(alert)
	print(image)
	context = {
	'alert_data':zip(alert,image),
	'slider_data':slimg,
	'branches':nosobj[0].branches,
	'awards':nosobj[0].awards,
	'missions':nosobj[0].missions,
	'something':nosobj[0].something,
	'slider_text_1':slider_text_1,
	'slider_text_2':slider_text_2,
	'slider_text_3':slider_text_3,
	'slider_text_4':slider_text_4,
	'fmr_description':fmr_description,
	'dm_description':dm_description,
	'bloodbank_description':bloodbank_description,
	'st_john_description':st_john_description,
	}
	return render(request,"index.html",context)

def post(request):
	post_name = request.get_full_path().split('/')[-1]
	post_name = re.sub('%20',' ',post_name)
	print(post_name)
	if post_name != '':
		obj = Post.objects.get(title__iexact=post_name)
		print(obj.content)

		url = []
		url = request.get_full_path().split('/')
		url = url[1:-1]
		# for f in url:
		# 	if f.lower() == 'home':
		# 		break
		# 	else:
		# 		url.remove(f)
		print(url)
		context = {
		'title':obj.title,
		'content':obj.content,
		'date':obj.date.strftime('%d-%m-%Y'),
		'category':obj.category,
		'url':url,
		}
		return render(request,"post.html",context)
	elif post_name == '':
		return render(request,"404.html")

def test(request):
	return render(request,"redcrossadmin.html")

# class Alerts(ListView):
# 	model = models.ModelDefinition
# 	context_object_name  = 'alert_list'
# 	template_name = 'alerts.html'

# list_alert = Alerts.as_view()

# class CreateAlert(CreateView):
# 	model = models.ModelDefinition
# 	template_name = 'alert_save.html'
# 	sucess_url = reverse_lazy('alert_list')

# create_alert = CreateAlert.as_view()

def upload(request):
	for count, x in enumerate(request.FILES.getlist("files")):
		def process(f):
			with open('C:\\Programming\\Django\\redcross\\redcross_media\\file_'+str(count),'wb+') as destination:
				for chunk in f.chunks():
					destination.write(chunk)
		process(x)
		return HttpResponse('Uploaded!')

def redcrossadmin(request):
	# top_slider_form = Top_SliderForm(request.POST or None)
	# team_image_form = Team_ImageForm(request.POST or None)
	alerts_form = AlertForm(request.POST or None)
	branch_form = BranchForm(request.POST or None)

	context = {
	# 'top_slider_form':top_slider_form,
	# 'team_image_form':team_image_form,
	'alerts_form':alerts_form,
	'branch_form':branch_form,
	}

	return render(request,"redcrossadmin.html",context)

def newsletter(request):
	obj = Newsletter.objects.all()
	newsletter = []
	file = []
	date = []
	
	url = []
	url = request.get_full_path().split('/')
	url = url[1:-1]
	for i in obj:
		newsletter.append(i.title)

		file.append(str(i.file).split('/')[-1])
		print(i.date.strftime('%d-%m-%Y'))
		date.append(i.date.strftime('%d-%m-%Y'))

	context = {
	'data':zip(newsletter,file,date),
	'url':url,
	}
	for x,y,z in zip(newsletter,file,date):
		print(x,"\t",y,"\t",z)

	return render(request,"newsletter.html",context)

def about(request):
	url = request.get_full_path().split('/')[-1]

	return render(request,url+".html")

def membership(request):
	return render(request,"membership.html")

def donate(request):
	return render(request,"donation.html")
def bloodbank(request):
	return render(request,"bloodbank.html")

def news(request):
	return render(request,"news.html")

def volunteer(request):
	return render(request,"volunteer.html")

def archive(request):
	return render(request,"archive.html")

def learn(request):
	# return render(request,"archive.html")
	pass
def news(request):
	return render(request,"news.html")

def gallery(request):
	return render(request,"gallery.html")

def dm(request):
	return render(request,"assoc1.html")

def icrc(request):
	return render(request,"assoc3_stjohn.html")

def stjohn(request):
	return render(request,"assoc4_icrc.html")