from django.contrib import admin
from .models import*
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display =('id','name','email','phone')
    list_display_links = ('name',)
    search_fields =('name','email')
    list_per_page = 25
admin.site.register(Contact,ContactAdmin)