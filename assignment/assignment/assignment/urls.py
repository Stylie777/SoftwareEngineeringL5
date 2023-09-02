"""
URL configuration for assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "myapp"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePage, name="Home"),
    path("register/", views.RegisterPage, name="Register"),
    path("login/", views.LoginPage, name="Login"),
    path("logout/", views.LogoutPage, name="Logout"),
    path("create_ticket/", views.CreateTicketPage, name="Create Ticket"),
    path("create_status/", views.CreateStatusPage, name="Create Status"),
    path("create_ticket_type/", views.CreateTicketTypePage, name="Create Ticket Type"),
    path("view_tickets/", views.ViewTickets, name="View Tickets"),
    path("view_ticket/<int:id>", views.ViewTicket, name="View Ticket"),
]

urlpatterns +=staticfiles_urlpatterns()
