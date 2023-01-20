from django.shortcuts import render
from .models import Student


def index(request):
    return render(request, 'students/index.html', {'student': Student.objects.all()})
