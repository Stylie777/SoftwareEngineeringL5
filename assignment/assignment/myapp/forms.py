import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket, Status, TicketType
from django.forms import ValidationError
import re

class NewUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

        widgets = {
            "username": forms.TextInput(attrs = {"class": "form-control"}),
            "email": forms.TextInput(attrs = {"class": "form-control"}),
            "first_name": forms.TextInput(attrs = {"class": "form-control"}),
            "last_name": forms.TextInput(attrs = {"class": "form-control"}),
            "password1": forms.TextInput(attrs = {"class": "form-control"}),
            "password2": forms.TextInput(attrs = {"class": "form-control"}),
        }

    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class AddTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("ticket_title", "ticket_info", "assignee", "status", "type", "date_due")

        widgets = {
            "ticket_title": forms.TextInput(attrs={"class":"form-control"}),
            "ticket_info": forms.Textarea(attrs={"class":"form-control"}),
            "assignee": forms.Select(attrs={"class":"form-control"}),
            "status": forms.Select(attrs={"class":"form-control"}),
            "type": forms.Select(attrs={"class":"form-control"}),
            "date_due": forms.DateInput(attrs={"class":"form-control"}, format="%d/%m/%y"),
        }

    def clean_ticket_title(self):
        ticket_title = self.cleaned_data["ticket_title"]

        if not check_capital_letter(ticket_title):
            raise ValidationError("Please enter the ticket title with the first letter as a Capital")

        return ticket_title

    def save(self, commit=True):
        ticket = super(AddTicket, self).save(commit=False)
        ticket.date_reported = datetime.date.today()

        if commit:
            ticket.save()
        return ticket

class AddStatus(forms.ModelForm):
    class Meta:
        model = Status
        fields = ("status_name", "status_description")

        widgets ={
            "status_name": forms.TextInput(attrs={"class":"form-control"}),
            "status_description": forms.Textarea(attrs= {"class":"form-control"}),
        }
    
    def clean_status_name(self):
        status_name = self.cleaned_data["status_name"]

        if not check_capital_letter(status_name):
            raise ValidationError("Please enter the ticket title with the first letter as a Capital")

        return status_name

    def save(self, commit=True):
        status = super(AddStatus, self).save(commit=False)

        if commit:
            status.save()
        return status

class AddTicketType(forms.ModelForm):
    class Meta:
        model = TicketType
        fields = {"type_name", "type_description"}

        widgets = {
            "type_name": forms.TextInput(attrs={"class":"form-control"}),
            "type_description": forms.Textarea(attrs={"class":"form-control"})
        }

    def clean_type_name(self):
        type_name = self.cleaned_data["type_name"]

        if not check_capital_letter(type_name):
            raise ValidationError("Please enter the type name with the first letter as a Capital")
        
        return type_name
    
    def save(self, commit=True):
        ticket_type = super(AddTicketType, self).save(commit=False)

        if commit:
            ticket_type.save()
        return ticket_type

def check_capital_letter(text):
    return bool(re.match(r"(^[A-Z]{1}[\w\s]*){1}", text))