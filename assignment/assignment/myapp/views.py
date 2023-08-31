from django.shortcuts import render, redirect
from .forms import NewUser, AddTicket, AddStatus, AddTicketType
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import re, datetime

def HomePage(request):
    return render(request, "myapp/home.html")

def RegisterPage(request):
    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("Home")
        messages.error(request, "Registration Unsuccessful, please proivde valid information.")
    
    form = NewUser()
    return render(request=request, template_name="myapp/register.html", context={"register_form":form})

def LoginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect("Home")
            else:
                messages.error(request, "Invalid Username or Password. Please try again.")
    form = AuthenticationForm()
    return render(request=request, template_name="myapp/login.html", context={"login_form":form})

def LogoutPage(request):
    logout(request)
    messages.info(request, "You have logged out.")
    return redirect("Home")

@login_required(login_url="/login")
def CreateTicketPage(request):
    form = AddTicket(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, message="Ticket logged")
        return redirect("Home")

    return render(request, 'myapp/add_ticket.html', context={"form":form})

@login_required(login_url="/login")
def CreateStatusPage(request):
    form = AddStatus(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Status Type Created")
        return redirect("Home")
    
    return render(request, "myapp/add_status.html", context={"form":form})

@login_required(login_url="/login")
def CreateTicketTypePage(request):
    form = AddTicketType(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Ticket Type Created")
        return redirect("Home")
    
    return render(request, "myapp/add_ticket_type.html", context={"form":form})