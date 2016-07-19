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

def one(request):
	print("hello")
	return render(request,"bloodbank/the_four1.html")

def two(request):
	return render(request,"bloodbank/the_four2.html")

def three(request):
	return render(request,"bloodbank/the_four3.html")

def four(request):
	return render(request,"bloodbank/the_four4.html")

def faq(request):
	return render(request,"bloodbank/faq.html")