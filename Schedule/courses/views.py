from django.shortcuts import render
import requests
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly
)
from .serializers import (
    CourseCreateUpdateSerializer,
    CouseDetailSerializer,
    StudentInfoSerialzier,
    )

from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,)
from rest_framework.response import Response
from .utils import spider,save_img
from .models import Course,Student
class CourseView(APIView):
    serializer_class = CourseCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    def post(self,request):
        serializer = CourseCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_stu_id = serializer.validated_data['user_stu_id']
        user_stu_pwd = serializer.validated_data['user_stu_pwd']

        yzm_text = serializer.validated_data['yzm_text']
        yzm_cookie = serializer.validated_data['yzm_cookie']
        user = request.user
        content ={}
        try:
            spider(user,user_stu_id,user_stu_pwd,yzm_text,yzm_cookie)
            content ={'msg':'Crawl the course successfully'}
            try:
                student = Student.objects.get(user=request.user)
            except:
                Student.objects.create(user=request.user, user_stu_id=user_stu_id, user_stu_pwd=user_stu_pwd)
                print "create successful!"
            return Response(content,HTTP_200_OK)
        except:
            content = {'error':'The password or captcha is wrong'}
            return Response(content,HTTP_400_BAD_REQUEST)
    def get(self,request):
        user = request.user
        queryset = Course.objects.filter(user=user)
        serializer = CouseDetailSerializer(queryset,data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        response = Response(serializer.data,HTTP_200_OK)
        return response


class YzmView(APIView):
    def get(self,request):
        username = request.user.username
        image_url = 'http://210.42.121.241/servlet/GenImg'
        yzm = requests.get(image_url)
        yzm_image = yzm.content
        save_img(username,yzm_image)
        yzm_url = "/media/yzm/"+str(username)+".jpg"
        yzm_cookie = yzm.headers['Set-Cookie']
        content ={}
        content['yzm_url'] = yzm_url
        content['yzm_cookie'] = yzm_cookie
        response = Response(content,HTTP_200_OK)
        return response

class StudentView(APIView):
    serializer_class = StudentInfoSerialzier
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    def get(self,request):
        user = request.user
        content = {}
        try:
            student =Student.objects.filter(user=user)
        except:
            content = {'error':'Not found this student'}
            return Response(content,HTTP_404_NOT_FOUND)
        serializer = StudentInfoSerialzier(student,data=request.data,many=True)

        serializer.is_valid(raise_exception=True)
        print serializer.data

        return Response(serializer.data,HTTP_200_OK)
