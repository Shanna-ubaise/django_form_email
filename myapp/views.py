from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Complaint
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings

def homepage(request):
    return render(request, 'myapp/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    context = {'registerform': form}
    return render(request, 'myapp/register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    context = {'loginform': form}
    return render(request, 'myapp/my-login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect("homepage") 

@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'myapp/dashboard.html')

@login_required(login_url="my-login")
def submit_complaint(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        purchase_date = request.POST.get('purchase_date')
        complaint_details = request.POST.get('complaint_details')

        # Save the complaint to the database
        complaint = Complaint.objects.create(
            product_name=product_name,
            purchase_date=purchase_date,
            complaint_details=complaint_details,
            user=request.user  
        )

        # Send a success email
        send_mail(
            'Complaint Registered Successfully',
            f'Your complaint about {product_name} has been registered successfully.',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False,
        )

        # Add a success message
        messages.success(request, 'Complaint successfully registered.')
        return redirect('dashboard')

   # return render(request, 'myapp/submit_complaint.html')
