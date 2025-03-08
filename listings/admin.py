from django.contrib import admin
from .models import*





class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','list_date','is_published','price','realtor')
    list_display_links=('title',)
    list_filter = ('realtor',)
    list_editable = ('is_published','price')
    search_fields = ('realtor','title')
    list_per_page = 10



admin.site.register(Listing,ListingAdmin)
