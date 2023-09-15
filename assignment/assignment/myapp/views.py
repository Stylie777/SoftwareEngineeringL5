from django.shortcuts import render, redirect
from .forms import NewUser, AddTicket, AddStatus, AddTicketType
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Ticket, Status, TicketType


def HomePage(request):
    """
    Renders the home page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the Django template
    """
    return render(request, "myapp/home.html")


def RegisterPage(request):
    """
    Renders the registration page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("Home")
        messages.error(
            request, "Registration Unsuccessful, please proivde valid information."
        )

    form = NewUser()
    return render(
        request=request,
        template_name="myapp/register.html",
        context={"register_form": form},
    )


def LoginPage(request):
    """
    Renders the login page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect("Home")
            else:
                messages.error(
                    request, "Invalid Username or Password. Please try again."
                )
    form = AuthenticationForm()
    return render(
        request=request, template_name="myapp/login.html", context={"login_form": form}
    )


@login_required(login_url="/login")
def LogoutPage(request):
    """
    Renders the logout page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    logout(request)
    messages.info(request, "You have logged out.")
    return redirect("Home")


@login_required(login_url="/login")
def CreateTicketPage(request):
    """
    Renders the create ticket page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    form = AddTicket(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, message="Ticket logged")
        return redirect("Home")

    return render(
        request, "myapp/form.html", context={"form": form, "title": "Create Ticket"}
    )


@login_required(login_url="/login")
def CreateStatusPage(request):
    """
    Renders the create status page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    form = AddStatus(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Status Type Created")
        return redirect("Home")

    return render(
        request, "myapp/form.html", context={"form": form, "title": "Create Status"}
    )


@login_required(login_url="/login")
def CreateTicketTypePage(request):
    """
    Renders the create ticket type page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    form = AddTicketType(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Ticket Type Created")
        return redirect("Home")

    return render(
        request,
        "myapp/form.html",
        context={"form": form, "title": "Create Ticket Type"},
    )


@login_required(login_url="/login")
def ViewTickets(request):
    """
    Renders the view tickets page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    tickets = Ticket.objects.all()
    return render(request, "myapp/display_tickets.html", {"tickets": tickets})


@login_required(login_url="/login")
def ViewTicket(request, id: int):
    """
    Renders the view ticket page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    ticket = Ticket.objects.get(ticket_id=id)
    return render(request, "myapp/display_ticket.html", {"ticket": ticket})


@login_required(login_url="/login")
def ViewStatuses(request):
    """
    Renders the view statuses page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    statuses = Status.objects.all()
    return render(request, "myapp/display_statuses.html", {"statuses": statuses})


@login_required(login_url="/login")
def ViewStatus(request, status_name):
    """
    Renders the view status page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    try:
        status_name.replace("%20", " ")
    except:
        pass
    status = Status.objects.get(status_name=status_name)
    return render(request, "myapp/display_status.html", {"status": status})


@login_required(login_url="/login")
def ViewTypes(request):
    """
    Renders the view types page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    types = TicketType.objects.all()
    return render(request, "myapp/display_types.html", {"types": types})


@login_required(login_url="/login")
def ViewType(request, type_name):
    """
    Renders the view type page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    try:
        type_name.replace("%20", " ")
    except:
        pass
    type = TicketType.objects.get(type_name=type_name)
    return render(request, "myapp/display_type.html", {"type": type})


@login_required(login_url="/login")
def UpdateTicket(request, id):
    """
    Renders the update ticket page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    instance = Ticket.objects.get(ticket_id=id)
    form = AddTicket(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        messages.success(request, message=f"Ticket {id} Updated")
        return redirect("View Tickets")
    return render(request, "myapp/form.html", {"form": form, "title": "Update Ticket"})


@login_required(login_url="/login")
def UpdateStatus(request, status_name):
    """
    Renders the update status page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
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
    return render(request, "myapp/form.html", {"form": form, "title": "Update Status"})


@login_required(login_url="/login")
def UpdateTicketType(request, type_name):
    """
    Renders the update ticket type page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
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
    return render(
        request, "myapp/form.html", {"form": form, "title": "Update Ticket Type"}
    )


@user_passes_test(lambda user: user.is_superuser)
def DeleteTicket(request, id):
    """
    Renders the delete ticket page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    ticket = Ticket.objects.get(ticket_id=id)

    if request.method == "POST":
        if "delete" in request.POST:
            ticket.delete()
            messages.success(request, message=f"Ticket {id} deleted")

        return redirect("View Tickets")

    return render(
        request,
        "myapp/delete_object.html",
        context={"model_name": "Ticket", "object_id": ticket.ticket_id},
    )


@user_passes_test(lambda user: user.is_superuser)
def DeleteStatus(request, status_name):
    """
    Renders the delete status page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    status = Status.objects.get(status_name=status_name)

    if request.method == "POST":
        if "delete" in request.POST:
            status.delete()
            messages.success(request, message=f"Status, {status_name}, deleted")

        return redirect("View Statuses")

    return render(
        request,
        "myapp/delete_object.html",
        context={"model_name": "Status", "object_id": status.status_name},
    )


@user_passes_test(lambda user: user.is_superuser)
def DeleteTicketType(request, type_name):
    """
    Renders the delete ticket type page

    Parameters:
        request: The webpage request
    
    Returns:
        : Render of the webpage using the django template
    """
    type = TicketType.objects.get(type_name=type_name)

    if request.method == "POST":
        if "delete" in request.POST:
            type.delete()
            messages.success(request, message=f"Type, {type_name}, deleted")

        return redirect("View Types")

    return render(
        request,
        "myapp/delete_object.html",
        context={"model_name": "Ticket Type", "object_id": type.type_name},
    )
