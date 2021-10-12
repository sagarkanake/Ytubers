from django.shortcuts import render
from .models import Slider, Team, Services, About
from youtubers.models import Youtuber
from contactInfo.models import ContactInfo

# Create your views here.


def home(request):
    contact = ContactInfo.objects.all()
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    ytubers = Youtuber.objects.order_by('-created_date')
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True) 
    data = {
        
        'contact': contact,
        'sliders': sliders,
        'teams': teams, 
        'ytubers': ytubers,
        'featured_youtubers': featured_youtubers,
        
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    sliders = Slider.objects.filter(headline= "Charity Event")
    
    teams =Team.objects.all()
    about = About.objects.all()
    contact = ContactInfo.objects.all()
    
    data = {
        'contact': contact,
        'teams': teams,
        'about': about,
        'sliders':sliders,
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    contact = ContactInfo.objects.all()
    teams =Team.objects.all()
    services = Services.objects.all()
    data = {
        'contact': contact,
        'teams': teams,
        'services': services,
    }
    return render(request, 'webpages/services.html', data)

def contact(request):  
    contact = ContactInfo.objects.all()
    
    ytubers = Youtuber.objects.order_by('-created_date')
    data = {
        'contact': contact,
        'ytubers': ytubers,
    }
    return render(request, 'webpages/contact.html', data)