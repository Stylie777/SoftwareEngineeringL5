from django.shortcuts import render, redirect
from .forms import NewUser, AddTicket, AddStatus, AddTicketType
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import re, datetime
from .models import Ticket, Status, TicketType

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

@login_required(login_url="/login")
def ViewTickets(request):
    tickets = Ticket.objects.all()
    return render(request, "myapp/display_tickets.html", {"tickets": tickets})

@login_required(login_url="/login")
def ViewTicket(request, id: int):
    ticket = Ticket.objects.get(ticket_id=id)
    return render(request, "myapp/display_ticket.html", {"ticket":ticket})

@login_required(login_url="/login")
def ViewStatuses(request):
    statuses = Status.objects.all()
    return render(request, "myapp/display_statuses.html", {"statuses": statuses})

@login_required(login_url="/login")
def ViewStatus(request, status_name):
    status_name.replace("%20", " ")
    status = Status.objects.get(status_name=status_name)
    return render(request, "myapp/display_status.html", {"status": status})

@login_required(login_url="/login")
def ViewTypes(request):
    types = TicketType.objects.all()
    return render(request, "myapp/display_types.html", {"types": types})

@login_required(login_url="/login")
def ViewType(request, type_name):
    try:
        type_name.replace("%20", " ")
    except:
        pass
    type = TicketType.objects.get(type_name=type_name)
    return render(request, "myapp/display_type.html", {"type": type})

@login_required(login_url="/login")
def UpdateTicket(request, id):
    instance = Ticket.objects.get(ticket_id=id)
    form = AddTicket(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        messages.success(request, message=f"Ticket {id} Updated")
        return redirect("View Tickets")
    return render(request, "myapp/update_ticket.html", {"form": form})

@login_required(login_url="/login")
def UpdateStatus(request, status_name):
    try:
        status_name.replace("%20", " ")
    except:
        pass
    instance = Status.objects.get(status_name=status_name)
    form = AddStatus(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        messages.success(request, message=f"Status, {status_name}, Updated")
        return redirect("View Statuses")
    return render(request, "myapp/update_status.html", {"form": form})

@login_required(login_url="/login")
def UpdateTicketType(request, type_name):
    try:
        type_name.replace("%20", " ")
    except:
        pass
    instance = TicketType.objects.get(type_name=type_name)
    form = AddTicketType(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        messages.success(request, message=f"Ticket Type, {type_name}, Updated")
        return redirect("View Types")
    return render(request, "myapp/update_type.html", {"form": form})
