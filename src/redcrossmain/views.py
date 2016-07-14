from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from .models import *
from .forms import *
import re

# Create your views here.
def home(request):
	try:
		alertobj = Alert.objects.all()
		sliderobj = os.listdir(os.path.join(settings.MEDIA_ROOT,"uploads","topslider"))
		slimg = []
		for a in sliderobj:
			slimg.append(a)
		alert = []
		image = []
		for i in alertobj:
			alert.append(i.title)
			image.append(i.image)

		nosobj = Branch_Number.objects.all()

		hometxtobj = Hometext.objects.all()
		read_more = ''
		slider_read_more = ''
		slider_text_1 = ''
		slider_text_2 = ''
		slider_text_3 = ''
		slider_text_4 = ''
		slider_text_5 = ''
		fmr_description = ''
		dm_description = ''
		st_john_description = ''
		bloodbank_description = ''
		for d in hometxtobj:
			slider_text_1 = d.slider_text_1
			slider_text_2 = d.slider_text_2
			slider_text_3 = d.slider_text_3
			slider_text_4 = d.slider_text_4
			slider_text_5 = d.slider_text_5
			slider_read_more = d.slider_read_more


			fmr_description = d.fmr_description
			dm_description = d.dm_description
			st_john_description = d.st_john_ambulance_description
			bloodbank_description = d.bloodbank_description
		if slider_read_more != None:
			read_more = True
		else:
			read_more = False
		print(read_more)
		#news
		k = 0
		title = []
		caption = []
		date = []
		link = []
		month = []
		year = []
		img = []
		for q1 in Post.objects.filter(category__iexact='news').order_by('-date'):
			if k < 3:
				title.append(q1.title)
				caption.append(q1.caption)
				date.append(q1.date.strftime('%d'))
				link.append(q1.title_slug)
				month.append(q1.date.strftime('%B'))
				year.append(q1.date.strftime('%Y'))
				img.append(q1.preview_image_name)
				k+=1
			else:
				break


		#newsletter
		newsletter = Newsletter.objects.all().order_by('date')[0]


		print(alert)
		print(img)
		context = {
		'alert':alert,
		'slider_data':slimg,
		'branches':nosobj[0].branches,
		'pmc':nosobj[0].pmc,
		'bb':nosobj[0].bb,
		'members':nosobj[0].members,
		'slider_text_1':slider_text_1,
		'slider_text_2':slider_text_2,
		'slider_text_3':slider_text_3,
		'slider_text_4':slider_text_4,
		'slider_text_5':slider_text_5,
		'slider_read_more':slider_read_more,
		'read_more':read_more,
		'fmr_description':fmr_description,
		'dm_description':dm_description,
		'bloodbank_description':bloodbank_description,
		'st_john_description':st_john_description,
		'newsdata':zip(title,caption,link,date,month,year,img),
		'newsletter':str(newsletter.file),
		}
		return render(request,"index.html",context)
	except Exception as e:
		print(e)
		raise Http404

def post(request):
	url = []
	url = request.get_full_path().split('/')
	for p in range(0,len(url)):
		url[p] = re.sub('%20','-',url[p])

	post_name = url[-1]
	url = url[1:-1]
	print(post_name)
	cat = ['news','red-cross-stories','relief','community','alerts','other','disaster']
	print(url)
	if post_name != '' and post_name.lower() not in cat:
		try:		
			obj = Post.objects.get(Q(title_slug__iexact=post_name) & Q(category__iexact=url[-1]))
			print(obj.title_slug)
			if obj.status == 'Publish':
				print(obj.status)
				url2 = ['../']
				for u in range(1,len(url)):
					url2.append(url2[u-1]+'../')

				
				url2 = url2[::-1]
				print(url2[1:])
				context = {
				'title':obj.title,
				'content':obj.content,
				'date':obj.date.strftime('%d-%m-%Y'),
				'category':obj.category,
				'caption':obj.caption,
				'url':zip(url[:-1],url2[1:]),
				}
				return render(request,"post.html",context)
			elif obj.status == 'Draft':
				print(obj.status)
				if request.user.is_superuser:				
					print(url)

					context = {
					'title':obj.title,
					'content':obj.content,
					'date':obj.date.strftime('%d-%m-%Y'),
					'category':obj.category,
					'url':zip(url,url2[::-1]),
					'l':'../',
					}

					return render(request,"post.html",context)
				else:
					raise Http404

		except Exception as e:
			print(e)
		raise Http404
	elif post_name != '' and post_name.lower() in cat:
		q = Post.objects.filter(category__iexact=post_name).order_by('-date')
		url2 = ['../']
		for u in range(1,len(url)):
			url2.append(url2[u-1]+'../')
		title = []
		caption = []
		date = []
		link = []
		month = []
		year = []
		titlef = []
		capf = []
		d = []
		m = []
		y = []
		lin = []
		img = []
		imgf = []
		print(url2)
		print(url)
		for q1 in q:
			if q1.featured == False:
				title.append(q1.title)
				caption.append(q1.caption)
				date.append(q1.date.strftime('%d'))
				link.append(q1.title_slug)
				month.append(q1.date.strftime('%B'))
				year.append(q1.date.strftime('%Y'))
				img.append(q1.preview_image_name)
			else:
				titlef.append(q1.title)
				capf.append(q1.caption)
				d.append(q1.date.strftime('%d'))
				m.append(q1.date.strftime('%B'))
				y.append(q1.date.strftime('%Y'))
				lin.append(q1.title_slug)
				imgf.append(q1.preview_image_name)
		#featured post
		print(img)
		print(titlef)
		print(title)
		if title or titlef:

			context = {
			'data':zip(title,caption,link,date,month,year,img),
			'category':post_name,
			'url':zip(url,url2),
			'l':'',
			'featured':zip(titlef,capf,d,m,y,lin,imgf),
			'ldata':zip(title[0:2],link[0:2],date[0:2],month[0:2],year[0:2],img[0:2]),
			}

			return render(request,"category.html",context)
		else:
			print("Empty")
			context = {
			'status':"Sorry No Posts, Come Back Later!"
			}
			return render(request,"empty.html",context)


	elif post_name == '':
		ab = Post.objects.all()
		url2 = ['#']
		
		
		context = {
		'data':ab,
		'url':zip(url,url2),
		}

		return render(request,"posthome.html",context)
	else:
		raise Http404

def test(request):
	return render(request,"redcrossadmin.html")


def redcrossadmin(request):
	alerts_form = AlertForm(request.POST or None)
	branch_form = BranchForm(request.POST or None)

	context = {
	'alerts_form':alerts_form,
	'branch_form':branch_form,
	}

	return render(request,"redcrossadmin.html",context)

def newsletter(request):
	obj = Newsletter.objects.all().order_by('-date')
	newsletter = []
	file = []
	date = []
	
	url = []
	url2 = ['']
	url = request.get_full_path().split('/')[1]

	for i in obj:
		newsletter.append(i.title)

		file.append(i.file)
		date.append(i.date.strftime('%d-%m-%Y'))

	context = {
	'data':zip(newsletter,file,date),
	'url':zip(url,url2),
	}

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
def rti(request):
	a = Rti.objects.all().order_by('-date')[0]
	context = {
	'content':a.rti,
	}
	return render(request,"rti.html",context)

def tender(request):
	a = Rti.objects.all().order_by('-date')[0]
	context = {
	'content':a.tenders,
	}
	return render(request,"rti.html",context)

def career(request):
	a = Rti.objects.all().order_by('-date')[0]
	context = {
	'content':a.career,
	}
	return render(request,"rti.html",context)


def search_title(request):

	print(request.POST.get('search_text',''))
	data = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text',''))

	return render_to_response('ajax_search.html',{'data':data})

def forms(request):	
	if request.method == "POST":
		form = BloodDonationForm(request.POST)
		print(request.method)
		print(request.POST)
		if form.is_valid():
			instance = form.save()
			# instance.save()
			for c in request.POST.getlist('disease_last_6_months'):
				instance.disease_last_6_months.save()
				form.save_m2m()
			for d in request.POST.getlist('taken_following_in_last_24_hrs'):
				instance.taken_following_in_last_24_hrs.save()
				form.save_m2m()
			for e in request.POST.getlist('suffered_any_of_these'):
				instance.suffered_any_of_these.save()
				form.save_m2m()
			for f in request.POST.getlist('for_women'):
				instance.for_women.save()

			form.save_m2m()
			print(instance.name)
			print(instance.age)
	

		context = { 
		'form':form,
		}
		return redirect('/')
	else:
		context = {
		'form':BloodDonationForm()
		}
		return render(request,"forms.html",context)

def events(request):
	obj = Event.objects.all()
	calender = []
	date = []
	desc = []
	print(obj)
	for i in obj:
		calender.append(i.event_name)
		date.append(i.date)
		desc.append(i.description)

	context = {
	'data':zip(calender,date,desc),
	}
	return render(request,"calendar.html",context)
