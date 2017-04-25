from django.conf.urls import url, include
from .views import (TaskListAPIView,
                    TaskDetailAPIView,
                    TaskCreateAPIView,
                    TaskUpdateAPIView,
                    TaskDeleteAPIView,
                    TaskWeekAPIView)
urlpatterns = [
    url(r'^$', TaskListAPIView.as_view(), name='list'),
    url(r'^week-list/$', TaskWeekAPIView.as_view(), name='week-list'),
    url(r'^create/$', TaskCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TaskDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit$', TaskUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$', TaskDeleteAPIView.as_view(), name='delete'),
]