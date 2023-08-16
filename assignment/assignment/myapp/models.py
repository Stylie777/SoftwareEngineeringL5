from django.db import models

class UserPermissions(models.Model):
    permissions_id = models.IntegerField(primary_key=True, null=False)
    persmission_name = models.CharField(max_length=50, null=False)

class UserGroups(models.Model):
    group_id = models.IntegerField(primary_key=True, null=False)
    group_name = models.CharField(max_length=50, null=False)
    permissions_id = models.ForeignKey(UserPermissions, on_delete=models.CASCADE)

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True, null=False)
    group_id = models.ForeignKey(UserGroups, on_delete=models.CASCADE)
    date_joined = models.DateField(null=False)
    email_address = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=1000, null=False)

class Tickets(models.Model):
    ticket_id = models.IntegerField(primary_key=True, null=False)
    ticket_details = models.CharField(max_length=100)
    ticket_description = models.CharField(max_length=2000)
    assignee_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)