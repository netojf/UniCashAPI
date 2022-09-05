from django.db import models

# Create your models here.
class Student(models.Model):
    StudentId = models.AutoField(primary_key = True)
    Enrollment = models.CharField(verbose_name='Matrícula', name='Matrícula', max_length=12)
    Password = models.CharField(max_length=36)
    Name = models.CharField(max_length=120, null=True)
