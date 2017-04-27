from django.http import Http404
from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import RetrieveAPIView
from .models import Notice, Membership
from .serializers import NoticeRetrieveSerializer, MembershipSerializer


class NoticeRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoticeRetrieveSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Notice.objects.filter(user=self.request.user)
        return queryset


class MembershipAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_notice_object(self, pk):
        try:
            notice = Notice.objects.get(pk=pk)
            return notice
        except Notice.DoesNotExist:
            raise Http404

    def get(self, request, notice_pk):
        notice = self.get_notice_object(pk=notice_pk)
        try:
            membership = Membership.objects.get(notice=notice, user=self.request.user)
            membership.is_send = True
            membership.save()
            serializer = MembershipSerializer(membership)
            return Response(serializer.data, status=HTTP_200_OK)
        except Membership.DoesNotExist:
            raise Http404
