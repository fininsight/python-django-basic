from django.shortcuts import render
from .models import Students, Scores

# Create your views here.
def students(request):
    data = Students.objects.all()

    return render(request, 'first/students.html', {
        'students': data
    })

def scores(request):
    data = Scores.objects.all()

    return render(request, 'first/scores.html', {
        'scores': data
    })