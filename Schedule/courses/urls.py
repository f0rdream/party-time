from django.conf.urls import url, include
from .views import (YzmView,CourseView,StudentView)
urlpatterns = [
    url(r'^yzm/$', YzmView.as_view(), name='yzm'),
    url(r'^$',CourseView.as_view(),name='courses'),
    url(r'^student/$',StudentView().as_view(),name='student'),
]