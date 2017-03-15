from .models import Notice, Membership
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class NoticeRetrieveSerializer(ModelSerializer):

    class Meta:
        model = Notice
        fields = [
            'id',
            'sender',
            'user',
            'groupname',
            'text',
            'time',
        ]


class MembershipSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Membership
        fields = [
            'user',
            'notice',
            'is_send',
        ]

    def get_user(self, obj):
        return str(obj.user.username)