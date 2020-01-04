from django.contrib import admin

from . import models
# Register your models here.

class Q(admin.ModelAdmin):
    list_display = ['id','question_text','pub_date']

class C(admin.ModelAdmin):
    list_display = ['id', 'question', 'choice_text','votes']

admin.site.register(models.Question,Q)
admin.site.register(models.Choice1,C)
