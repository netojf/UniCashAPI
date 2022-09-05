from ast import Delete
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from StudentApp.models import Student
from StudentApp.serializers import StudentSerializer

@csrf_exempt
def StudentAPI(request, id=0):
    if request.method == 'GET':
        students = Student.objects.all()
        students_serializer = StudentSerializer(students,many=True)
        return JsonResponse(students_serializer.data,safe=False)
    
    
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        students_serializer=StudentSerializer(date=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    
    elif request.method=='PUT':
        student_data = JSONParser().parse(request)
        student=Student.objects.get(StudentId=student_data['StudentId'])
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('Registry Updated Successfully!', safe=False)
        return JsonResponse('An Error occured Updating Registry', safe=False)
    
    
    elif request.method=='DELETE':
        student_data = JSONParser().parse(request)
        student=Student.objects.get(StudentId=student_data['StudentId'])
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.Delete()
            return JsonResponse('Registry Deleted Successfully!', safe=False)
        return JsonResponse('An Error occured Deleting Registry', safe=False)
# Create your views here.
