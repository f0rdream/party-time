from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
class Student(models.Model):
    user = models.OneToOneField(User)
    user_stu_id = models.CharField(max_length=20,blank=False)
    user_stu_pwd = models.CharField(max_length=100,blank=False)
class Course(models.Model):
    user = models.ForeignKey(User)
    stu_name = models.CharField(max_length=100,blank=True,null=True)
    stu_term = models.CharField(max_length=100,blank=True,null=True)
    course_num = models.CharField(max_length=100,blank=True,null=True)
    course_name = models.CharField(max_length=100,blank=True,null=True)
    course_type = models.CharField(max_length=100,blank=True,null=True)
    course_college = models.CharField(max_length=100,blank=True,null=True)
    course_teacher = models.CharField(max_length=100,blank=True,null=True)
    course_major = models.CharField(max_length=100,blank=True,null=True)
    course_point = models.CharField(max_length=100,blank=True,null=True)
    day = models.CharField(max_length=100,blank=True,null=True)
    start_num = models.CharField(max_length=100,blank=True,null=True)
    end_num = models.CharField(max_length=100,blank=True,null=True)

# Create your models here.
