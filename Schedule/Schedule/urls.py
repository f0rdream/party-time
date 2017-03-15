"""Schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from websocket_message.views import NoticeRetrieveAPIView, MembershipAPIView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'auth/token/', obtain_jwt_token),
    url(r'tasks/', include('tasks.urls', namespace='tasks')),
    url(r'accounts/',include('accounts.urls', namespace='accounts')),
    url(r'group-agenda/', include('groupagenda.urls', namespace='groupagenda')),
    url(r'notice/(?P<pk>\d+)/$', NoticeRetrieveAPIView.as_view(), name="notice"),
    url(r'membership/(?P<notice_pk>\d+)/$', MembershipAPIView.as_view(), name="membership"),

]
