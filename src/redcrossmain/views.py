from django.shortcuts import render
from django.conf import settings
from .models import *

# Create your views here.
def home(request):
	return render(request,"index.html")

def post(request):
	# post_name = request.get_full_path().split('/')[-1]
	obj = Post.objects.get(title='test')
	context = {
	'title':obj.title,
	'content':obj.content,
	'date':obj.date
	}
	return render(request,"post.html",context)