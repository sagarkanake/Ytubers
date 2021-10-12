from django.shortcuts import redirect, render
from .models import Contacttuber
from youtubers.models import Youtuber
from django.contrib import messages
# Create your vieemail



    


def contacttuber(request):
    tuber_search = Youtuber.objects.values_list('name', flat=True).distinct() 
    
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        tuber_name = request.POST['tuber_name']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']
        
        # TODO: do all sanitzation 
        
        contacttuber = Contacttuber(
            full_name=full_name, phone=phone, email=email, company_name=company_name, tuber_name=tuber_name, subject=subject, message=message, user_id=user_id )
        contacttuber.save()
        messages.success(request, "Thanks for reaching out")
        return redirect('youtubers')
    
    

        
    
    