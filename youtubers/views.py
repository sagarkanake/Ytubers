from django.shortcuts import get_object_or_404, render
from .models import Youtuber
from contactInfo.models import ContactInfo
from django.db.models import Q

# Create your views here.
def youtubers_3(request):
    contact = ContactInfo.objects.all()
    tubers = Youtuber.objects.filter(pk__in=[6,7,8,9])
    
    #tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            tubers = tubers.filter(age__iexact=age)
    data = {
        'contact':contact,
        'tubers': tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    return render(request, 'youtubers/youtubers_3.html', data)

def youtubers_2(request):
    contact = ContactInfo.objects.all()
    tubers = Youtuber.objects.filter(pk__in=[5,6,8,9])
    
    #tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            tubers = tubers.filter(age__iexact=age)
    data = {
        'contact':contact,
        'tubers': tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    return render(request, 'youtubers/youtubers_2.html', data)
    
    
def youtubers_1(request):
    contact = ContactInfo.objects.all()
    
    tubers = Youtuber.objects.filter(pk__in=[3,4,8,9])
    
    #tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            tubers = tubers.filter(age__iexact=age)
    
    data = {
        'contact':contact,
        'tubers': tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    return render(request, 'youtubers/youtubers_1.html', data)
    
def youtubers(request):
    contact = ContactInfo.objects.all()
    tubers1 = Youtuber.objects.filter(pk__in=[1,2,8,9])
    
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            tubers = tubers.filter(age__iexact=age)
            
    data = {
        'contact': contact,
        #'tubers': tubers,
        'tubers1':tubers1,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    contact = ContactInfo.objects.all()
    
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'contact':contact,
        'tuber': tuber,
    }
    return render(request, 'youtubers/youtubers_detail.html', data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    age_search = Youtuber.objects.values_list('age', flat=True).distinct()
    crew_search = Youtuber.objects.values_list('crew', flat=True).distinct()
    contact = ContactInfo.objects.all()
    
    
    
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            tubers = tubers.filter(age__iexact=age)
            
            
    if 'crew' in request.GET:
        crew = request.GET['crew']
        if crew:
            tubers = tubers.filter(crew__iexact=crew)    
                
            
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(Q(description__icontains=keyword)|Q(name__icontains=keyword)|Q(crew__icontains=keyword))
    
    
    
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
            
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
            
                    
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)        
    
    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search,
        'age_search': age_search,
        'crew_search':crew_search,
         
        'contact':contact, 
        
        
        
    }
    return render(request, 'youtubers/search.html', data)