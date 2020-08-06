from django.shortcuts import render
from .models import Students

# Create your views here.
def students(request):
    data = Students.objects.all()

    return render(request, 'first/students.html', {
        'students': data
    })