from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
        announcement_id = request.POST['announcement_id']
        announcement = request.POST['announcement']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        official_email = request.POST['official_email']

        #Check if user has made an inquiry
        if request.user.is_authenticated:
                user_id = request.user.id 
                has_contacted = Contact.objects.all().filter(announcement_id=announcement_id,
                                                             user_id=user_id,
                                                             )
                if has_contacted:
                        messages.error(request, 'You have already made an inquiry for this announcement')
                        return redirect('/announcements/'+ announcement_id)
                                
        contact = Contact(announcement_id=announcement_id,
                          announcement=announcement,
                          name=name,
                          email=email,
                          phone=phone,
                          message=message,
                          user_id=user_id)
                
        contact.save()
        

        messages.success(request, 'Your request has been submitted')
        return redirect('/announcements/'+ announcement_id)
