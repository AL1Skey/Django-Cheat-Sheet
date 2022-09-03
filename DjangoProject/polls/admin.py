from django.contrib import admin

# Register your models here.
from .models import Quest,Option

#Registering models

#admin.site.register(Quest)
#admin.site.register(Option)

admin.site.site_header = "Polls Administrator"
admin.site.site_title = "Polls Admin"
admin.site.index_title = "Welcome to Polls Admin"

class ChoiceInline(admin.TabularInline):
    model = Option

class QuestionManager(admin.ModelAdmin):
    fieldsets=[('Question',{'fields':['quest_text']}),
    ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    
    ]
    inlines=[ChoiceInline]

admin.site.register(Quest,QuestionManager)