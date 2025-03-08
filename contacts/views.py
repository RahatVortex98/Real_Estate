from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')

        if not listing:
            messages.error(request, 'Listing field is required')
            return redirect('/listings/' + listing_id)

        # Check if the user has already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id).exists()
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )
        contact.save()
        send_mail(
            'Property Inquiry',
            f'There has been an inquiry for {listing}. Sign into the admin panel for more info.',
            'your-email@gmail.com',  # From email
            [realtor_email],  # To email
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/' + listing_id)
    else:
        return redirect('listings')  # Redirect to listings page if not a POST request