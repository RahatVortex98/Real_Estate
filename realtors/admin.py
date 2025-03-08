from django.contrib import admin
from .models import*


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name',)





admin.site.register(Realtor,RealtorAdmin)