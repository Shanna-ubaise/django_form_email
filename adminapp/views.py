from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate
from .models import tb1_Authentication
from myapp.models import *
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def base(request):
    
    return render(request, 'base.html')

def owner(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = tb1_Authentication.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return render(request, 'loginsuccess.html')
            else:
                print(f"Login failed for user: {username}")
                return redirect('/')
        except tb1_Authentication.DoesNotExist:
            print(f"User does not exist: {username}")
            return redirect('/')
        except Exception as e:
            print(f"An error occurred: {e}")
            return redirect('/')
    else:
        return render(request, 'base.html')
class login(View):
    def get(self,request):
        complaint = Complaint.objects.all()
        context = {"complaint":complaint}
        return render(request, 'loginsuccess.html',context)
    
def homepage(request):
    return render(request, 'logout.html')




 

