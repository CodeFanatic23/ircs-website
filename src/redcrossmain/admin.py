from django.contrib import admin
from django.utils.html import format_html
from .models import *
from .forms import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','category','date','Status','show_firm_url']
	search_fields = ['title','category']
	list_filter = ['category','status']
	actions = ['preview']
	# model = Post
	def Status(self,obj):
		if obj.status == 'Publish':
			return obj.status + 'ed'
		else:
			return obj.status
	def show_firm_url(self, obj):
		return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.link_to_post)
	
	show_firm_url.short_description = "Link To Post"

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

	# def get_actions(self, request):

	# 	actions = super(BranchNumberAdmin, self).get_actions(request)

		# del actions['delete_selected']

		# return actions

	# def has_delete_permission(self, request, obj=None):
	# 	#Disable delete
	# 	return False

	# def has_add_permission(self,request):
	# 	return False

class HometextAdmin(admin.ModelAdmin):
	list_display = ['updated']

	model = Hometext

class RtiAdmin(admin.ModelAdmin):
	list_display = ['date']

class BloodDonationAdmin(admin.ModelAdmin):
	list_display = ['name','age','mobile_number','blood_group']

	# model = BloodDonation
	form = BloodDonationForm
class EventAdmin(admin.ModelAdmin):
	list_display = ['event_name','date']

	model = Event

class GalleryAdmin(admin.ModelAdmin):
	list_display = ['album_name']

	model = Gallery
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(BloodDonation,BloodDonationAdmin)
admin.site.register(Rti,RtiAdmin)
admin.site.register(Hometext,HometextAdmin)
admin.site.register(Top_Slider,TopSliderAdmin)
admin.site.register(Team_Images,TeamImagesAdmin)
admin.site.register(Alert,AlertAdmin)
admin.site.register(Newsletter,NewsletterAdmin)
admin.site.register(Branch_Number,BranchNumberAdmin)




	
