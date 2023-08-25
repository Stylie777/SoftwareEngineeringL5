from django.contrib import admin
from myapp.models import Status, TicketType, Ticket

admin.site.register(Status)
admin.site.register(TicketType)
admin.site.register(Ticket)
