from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import CustomUser, UserProfile

class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')
    
    def post(self, request):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
       
        errors = {}
        if not email:
            errors['email'] = 'Email is required'
        if CustomUser.objects.filter(email=email).exists():
            errors['email'] = 'Email already exists'
        if not username:
            errors['username'] = 'Username is required'
        if not password1:
            errors['password1'] = 'Password is required'
        if password1 != password2:
            errors['password2'] = 'Passwords do not match'
        
        if errors:
            return render(request, 'accounts/register.html', {'errors': errors, 'data': request.POST})
        
        # Create user
        user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password1
        )
        
      
        UserProfile.objects.create(user=user)
        
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'accounts/login.html', {'email': email})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home')
