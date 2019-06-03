from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from .models import BgyResident

def register(request):
    if request.method == 'POST':
        #get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if password match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name )
                user.save()
                messages.success(request,'You are now registered')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
    return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts' : user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def manage_profile(request):
        if request.method == 'POST':
            # Get form values
            resident = BgyResident()
            
            resident.birthdate= request.POST['birthdate']
            resident.birthplace = request.POST['birthplace']
            resident.address = request.POST['address']
            resident.gender = request.POST['gender']
            resident.philhealth = request.POST['philhealth']
            resident.highest_education= request.POST['highest_education']
            resident.remarks= request.POST['remarks']
            resident.phonenumber= request.POST['phonenumber']
            resident.file_upload = request.POST['file_upload']
            resident.photo_main = request.POST['photo_main']
            resident.user_id = request.user.id

            resident.save()
            messages.success(request,'Profile updated')
            return redirect('accounts_view')
        else:
            return render(request, 'accounts/manage_profile.html')

def accounts_view(request):
    user_id = request.user.id 
    resident = get_object_or_404(BgyResident, user_id=user_id)
    return render(request, 'accounts/accounts_view.html', {'resident' : resident})