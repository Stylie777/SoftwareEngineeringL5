from django.shortcuts import render
from django.views.generic.list import ListView
from f1_database.models import Team

class TeamListView(ListView):
    model = Team
    paginate_by = 10



