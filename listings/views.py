from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import*
from .choices import bedroom_choices,state_choices,price_choices

# Create your views here.
def listings(request):
    listings = Listing.objects.all()

    # Number of listings per page
    paginator = Paginator(listings, 3)  # Change 3 to any number of listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings  # Pass paginated listings to template
    }

    return render(request, 'listings/listings.html', context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)

    context ={
        'listing':listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    queryset = Listing.objects.order_by('-list_date')

    # Filtering Listings
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset = queryset.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset = queryset.filter(city__icontains=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset = queryset.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset = queryset.filter(bedrooms__gte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset = queryset.filter(price__lte=price)

    # Paginate the filtered results
    paginator = Paginator(queryset, 3)  # Show 3 listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': paged_listings,
        'values': request.GET  # To keep the form values after submitting
    }

    return render(request, 'listings/search.html', context)