from django.shortcuts import render
from django.http import  JsonResponse
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.

# api view 
@api_view(['GET', 'POST'])
def studentsViews(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailViews(request, pk):
    try:
        student = Student.objects.get(Student_id=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data, status=status.HTTP_200_OK)


# PUT request 

    elif request.method == 'PUT':
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method ==  'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
        