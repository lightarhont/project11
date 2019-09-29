from django.contrib import admin

from .models import *

class NVideoFields(admin.StackedInline):
    model = PageVideo

class NTextFields(admin.StackedInline):
    model = PageText

class NAudioFields(admin.StackedInline):
    model = PageAudio

class TextFields(admin.ModelAdmin):
    search_fields = ['title']

class VideoFields(admin.ModelAdmin):
    search_fields = ['title']

class AudioFields(admin.ModelAdmin):
    search_fields = ['title']

class PageFields(admin.ModelAdmin):
    inlines = [NVideoFields, NTextFields, NAudioFields]
    search_fields = ['title']

# Register your models here.
admin.site.register(Text, TextFields)
admin.site.register(Video, VideoFields)
admin.site.register(Audio, AudioFields)
admin.site.register(Page, PageFields)