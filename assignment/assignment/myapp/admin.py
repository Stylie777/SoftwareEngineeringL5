from django.contrib import admin
from myapp.models import UserGroups, UserPermissions, Users, Tickets

admin.site.register(Users)
admin.site.register(UserGroups)
admin.site.register(UserPermissions)
admin.site.register(Tickets)
