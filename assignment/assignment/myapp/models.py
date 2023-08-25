from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    status_id = models.AutoField(primary_key=True, null=False)
    status_description = models.CharField(max_length=50)

class TicketType(models.Model):
    type_name = models.CharField(max_length=20, null=False, primary_key=True)
    type_description = models.CharField(max_length=100, null=False)

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True, null=False)
    ticket_title = models.CharField(max_length=100, null=False)
    ticket_info = models.CharField(max_length=2000, null=False)
    assignee = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    date_reported = models.DateField(null=False)
    date_due = models.DateField()
