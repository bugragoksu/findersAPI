from django.contrib import admin
from .models import *
# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
        list_display = ['ownerId','title']
        list_display_links = ['ownerId','title']
        search_fields = ['ownerId','title','description']



class LocationAdmin(admin.ModelAdmin):
        list_display = ['city','latitude','longitude']
        list_display_links = ['city']
        search_fields = ['city']

class HumanAdmin(admin.ModelAdmin):
        list_display = ['name','surname']
        list_display_links = ['name']
        search_fields = ['name','surname']

class AnimalAdmin(admin.ModelAdmin):
        list_display = ['animalType','race','color']
        list_display_links = ['animalType']
        search_fields = ['animalType','race','color']


admin.site.register(Notice,NoticeAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Human,HumanAdmin)
admin.site.register(Animal,AnimalAdmin)