from django.db import models

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True, null=False)
    group_name = models.CharField(max_length=50)
    date_joined = models.DateField(null=False)
    email_address = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=1000, null=False)
