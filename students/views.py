from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

# web app view
def students(request):

    students = [
        {
            'name': "Ulrich Armel",
            'id': 1,
            'age': 23
        }
    ]
    return HttpResponse(students)

