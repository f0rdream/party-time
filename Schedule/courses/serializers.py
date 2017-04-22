from rest_framework.serializers import (
    SerializerMethodField,
    ModelSerializer,
    ValidationError,
    DateTimeField,
    CharField,
    )
from rest_framework import serializers
from .models import Student,Course
class CourseCreateUpdateSerializer(ModelSerializer):
    yzm_cookie = CharField()
    yzm_text =  CharField()
    user_stu_pwd = CharField(label='Password',
                         write_only=True,
                         style={'input_type': 'password'})
    class Meta:
        model = Student
        fields = [
            'user_stu_id',
            'user_stu_pwd',
            'yzm_text',
            'yzm_cookie',
        ]
    def validate(self, data):
        user_stu_id = data.get('user_stu_id')
        user_stu_pwd = data.get('user_stu_pwd')
        yzm_text = data.get('yzm_text')
        yzm_cookie = data.get('yzm_cookie')
        if not user_stu_id:
            raise ValidationError('lack user_stu_id')
        if not user_stu_pwd:
            raise ValidationError('lack user_stu_pwd')
        if not yzm_text:
            raise ValidationError('lack yzm_text')
        if not yzm_cookie:
            raise ValidationError('lack yzm_cookie')
        return data

class CouseDetailSerializer(ModelSerializer):
    username = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'username',
            'stu_name',
            'stu_term',
            'course_name',
            'course_num',
            'course_type',
            'course_college',
            'course_teacher',
            'course_major',
            'course_point',
            'day',
            'start_num',
            'end_num',
        ]
    def get_username(self,obj):
        return str(obj.user.username)
class StudentInfoSerialzier(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'user_stu_id',
            'user_stu_pwd',
        ]