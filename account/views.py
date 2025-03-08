from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth

from contacts.models import Contact

# Create your views here.
def login(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username,password=password)
       if user is not None:
            auth.login(request,user)
            messages.success(request,"Logged In")
            return redirect('dashboard')
       else:
           messages.error(request,'Invalid Credentials')
           return redirect('login')

       
    else:
        return render(request,'account/login.html')



def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"Logged Out")
        return redirect('index')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('register')

        # If all checks pass, create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(request, 'You are now registered and can log in')
        return redirect('login')

    return render(request, 'account/register.html')

   



def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts  # Corrected variable name
    }
    return render(request, 'account/dashboard.html', context)