# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import timedelta
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.create(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = username  # Store the username in the session
            return redirect('task')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def task(request):
    username = request.session.get('username', None)
    if not username:
        return redirect('login')  # Redirect to login if username is not in the session

    context = {'username': username}
    return render(request, 'task.html', context)

@csrf_exempt
def elapsed_time_view(request):
    if request.method == 'POST':
        elapsed_time_ms = int(request.POST.get('elapsed_time', 0))
        elapsed_time = timedelta(milliseconds=elapsed_time_ms)
        return JsonResponse({'elapsed_time': str(elapsed_time)})

    return render(request, 'task.html')  # Redirect to task.html for simplicity