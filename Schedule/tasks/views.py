from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from django.utils.timezone import datetime as dt
from django.utils import timezone
from .serializers import TaskListSerializer,TaskDetailSerializer,TaskCreateUpdateSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from .models import Task
from .permissions import MyIsAuthenticated
from rest_framework.authentication import SessionAuthentication
import datetime
# from django.utils.timezone import datetime as dt

# from django.shortcuts import render
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.


class TaskListAPIView(ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset


class TaskDetailAPIView(RetrieveAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset


class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    """
        About create views: there are some issue about POST.
        Do about it later.
    """
    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user
    #     username = user.username
    #     # user_obj = User.objects.filter(username="qwert")
    #     user_obj = User.objects.filter(username=username)
    #     queryset = Task.objects.filter(user=user_obj)
    #     return queryset
    #
    # def perform_create(self, serializer):
    #     user = self.request.user
    #     username = user.username
    #     user_obj = User.objects.filter(username=username)
    #     serializer.save(user=user_obj)


class TaskUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TaskCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset


class TaskDeleteAPIView(DestroyAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = [MyIsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self,*args,**kwargs):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset


class TaskWeekAPIView(APIView):
    """ api for task in a week"""
    first_day = dt.combine(datetime.date.today(), datetime.time())
    second_day = dt.combine(datetime.date.today()+datetime.timedelta(days=1), datetime.time())
    third_day = dt.combine(datetime.date.today()+datetime.timedelta(days=2), datetime.time())
    fourth_day = dt.combine(datetime.date.today()+datetime.timedelta(days=3), datetime.time())
    fifth_day = dt.combine(datetime.date.today()+datetime.timedelta(days=4), datetime.time())
    sixth_day = dt.combine(datetime.date.today()+datetime.timedelta(days=5), datetime.time())
    seventh_day = dt.combine(datetime.date.today()+datetime.timedelta(days=6), datetime.time())
    eighth_day = dt.combine(datetime.date.today()+datetime.timedelta(days=7), datetime.time())

    def get_queryset(self, day1, day2):
        user = self.request.user
        queryset = Task.objects.filter(user=user, start_time__range=(day1, day2))
        return queryset

    def get_serializer(self, day1, day2):
        queryset = self.get_queryset(day1=day1,day2=day2)
        serializer = TaskListSerializer(queryset, context={'request': self.request}, many=True)
        return serializer.data

    def get(self, request, *args, **kwargs):
        week_dict = {
            'first_day': self.get_serializer(self.first_day, self.second_day),
            'second_day': self.get_serializer(self.second_day, self.third_day),
            'third_day': self.get_serializer(self.third_day, self.fourth_day),
            'fourth_day': self.get_serializer(self.fourth_day, self.fifth_day),
            'fifth_day': self.get_serializer(self.fifth_day, self.sixth_day),
            'sixth_day': self.get_serializer(self.sixth_day, self.seventh_day),
            'seventh_day': self.get_serializer(self.seventh_day, self.eighth_day)
        }
        return Response(week_dict, status=HTTP_200_OK)

