# Django Imports
from django.shortcuts import render


def index(request):
    return render(request, "workshop_app/index.html")
