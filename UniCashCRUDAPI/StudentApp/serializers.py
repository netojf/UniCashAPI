from dataclasses import field
from rest_framework import serializers
from StudentApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('StudentId','Enrollment','Name')