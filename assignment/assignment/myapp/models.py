from django.db import models

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True, null=False)
    group_id = models.IntegerField()
    date_joined = models.DateField(null=False)
    email_address = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=1000, null=False)

class Tickets(models.Model):
    ticket_id = models.IntegerField(primary_key=True, null=False)
    ticket_details = models.CharField(max_length=100)
    ticket_description = models.CharField(max_length=2000)
    assignee_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)