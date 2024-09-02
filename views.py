# accounts/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserRole

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # 로그인 성공 시 기본적으로 대시보드로 이동
        else:
            # 로그인 실패 시 처리 로직
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')



@login_required
def dashboard(request):
    if request.user.role == UserRole.NON_MEMBER:
        return redirect('non_member_dashboard')
    elif request.user.role == UserRole.MEMBER:
        return redirect('member_dashboard')
    elif request.user.role == UserRole.EXECUTIVE:
        return redirect('executive_dashboard')
    else:
        return redirect('default_dashboard')
    
def default_dashboard(request):
    return render(request, 'default_dashboard.html')

def non_member_dashboard(request):
    return render(request, 'non_member_dashboard.html')

def member_dashboard(request):
    return render(request, 'member_dashboard.html')

def executive_dashboard(request):
    return render(request, 'executive_dashboard.html')
