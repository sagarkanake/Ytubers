from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from hiretubers.models import Hiretuber
from contactInfo.models import ContactInfo
from youtubers.models import Youtuber
from django.db.models import Q




def login(request):
    contact = ContactInfo.objects.all()
    
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.warning(request, 'Your are Logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('login')    
    
    data = {
        'contact': contact,
    }
        
    return render(request, 'acc/login.html', data)


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
                    
        else:
            messages.warning(request, 'Password do not match')
            return redirect('register')
        
       
    
    return render(request, 'acc/register.html')
    


def logout_user(request):
    logout(request)
    return redirect('home')
    
def ex(request):
    return render(request, 'acc/ex.html')


@login_required(login_url='login')
def dashboard(request):
    username = request.user.username
    current_user = request.user.email 
    c1 = request.user.last_name
    username = ''.join([i for i in username if not i.isdigit()])
    hiretuber = Hiretuber.objects.filter(Q(email=current_user)&Q(last_name__icontains=c1)) 
    ytubers = Youtuber.objects.all()
    
    contact = ContactInfo.objects.all()
    data = {
        'username': username,
        'ytubers': ytubers,
        'hiretuber': hiretuber,
        'contact': contact,
    }
    return render(request, 'acc/dashboard.html', data)
    