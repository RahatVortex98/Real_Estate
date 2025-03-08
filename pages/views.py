from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices,state_choices,price_choices

# Create your views here.
def index(request):
    listings =Listing.objects.filter(is_published=True)[:3]

    context={
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(request,'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    realtor_mvp =Realtor.objects.all().filter(is_mvp=True)

    context ={
        'realtors':realtors,
        'realtor_mvp': realtor_mvp
    }
    return render(request,'pages/about.html',context)