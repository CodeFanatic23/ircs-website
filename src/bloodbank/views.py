from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,"bloodbank.html")
def statistics(request):
	return render(request,"statistics.html")

def downloads(request):
	return render(request,"downloads.html")

def gallery(request):
	return render(request,"bloodbank/gallery.html")

def about(request):
	return render(request,"bloodbank/about.html")