from django.shortcuts import render
from django.http import HttpResponse
from announcements.models import Announcement
from officials.models import Official

def index(request):
    announcements = Announcement.objects.order_by('-date').filter(is_published=True)[:3]
    context = {
        'announcements' : announcements,
    }
    return render(request, 'pages/index.html', context)
    
def about(request):
    # Get all officials
    officials = Official.objects.order_by('-term_date')

    # Get MVP
    mvp_officials = Official.objects.all().filter(is_mvp=True)
    context = {
        'officials': officials,
        'mvp_officials' : mvp_officials
    }
    return render(request, 'pages/about.html', context)

