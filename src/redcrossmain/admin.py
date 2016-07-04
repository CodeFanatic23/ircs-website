from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','date']

	model = Post
	# form = PostForm

admin.site.register(Post,PostAdmin)
