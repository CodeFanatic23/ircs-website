from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','category','date','Status']
	search_fields = ['title','category']
	list_filter = ['category','status']
	actions = ['preview']
	# model = Post
	def Status(self,obj):
		if obj.status == 'Publish':
			return obj.status + 'ed'
		else:
			return obj.status

	# def preview(modeladmin, request, queryset):
	# 	get queryset by last updated
	# 	return  render(request,"post.html",context)
	form = PostForm

admin.site.register(Post,PostAdmin)

class TopSliderAdmin(admin.ModelAdmin):
	# list_display = ['date']

	model = Top_Slider

	def has_add_permission(self,request):
		return False

	def get_actions(self, request):

		actions = super(TopSliderAdmin, self).get_actions(request)

		del actions['delete_selected']

		return actions

	def has_delete_permission(self, request, obj=None):
		#Disable delete
		return False

class TeamImagesAdmin(admin.ModelAdmin):
	list_display = ['date']
	model = Team_Images

	# def has_add_permission(self,request):
	# 	return False

class AlertAdmin(admin.ModelAdmin):
	list_display = ['title','date']
	model = Alert


	# def has_add_permission(self,request):
	# 	return False
class NewsletterAdmin(admin.ModelAdmin):
	list_display = ['title','date']
	search_fields = ['title']
	model = Newsletter

class BranchNumberAdmin(admin.ModelAdmin):
	list_display = ['__str__']

	form = BranchForm

	def get_actions(self, request):

		actions = super(BranchNumberAdmin, self).get_actions(request)

		del actions['delete_selected']

		return actions

	def has_delete_permission(self, request, obj=None):
		#Disable delete
		return False

	# def has_add_permission(self,request):
	# 	return False

class HometextAdmin(admin.ModelAdmin):
	list_display = ['updated']

	model = Hometext

class RtiAdmin(admin.ModelAdmin):
	list_display = ['date']
admin.site.register(Rti,RtiAdmin)
admin.site.register(Hometext,HometextAdmin)
admin.site.register(Top_Slider,TopSliderAdmin)
admin.site.register(Team_Images,TeamImagesAdmin)
admin.site.register(Alert,AlertAdmin)
admin.site.register(Newsletter,NewsletterAdmin)
admin.site.register(Branch_Number,BranchNumberAdmin)




	
