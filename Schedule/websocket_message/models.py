#-*- coding:UTF-8 -*-
#消息通知类
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,Permission,Group,ContentType


class Notice(models.Model):
    sender = models.TextField()#消息的发送者
    user = models.ManyToManyField(User,through='Membership')
    groupname = models.TextField()#小组名字
    text = models.TextField()#消息内容
    time = models.DateTimeField(default=timezone.now, db_index=True)
    # def as_dict(self):
    #     return {'handle': self.username, 'message': self.message}

    def __unicode__(self):
        string = ""
        string += self.sender
        string += "-"
        string += self.groupname
        string += "-"
        string += str(self.pk)
        return string

class Membership(models.Model):
    # 消息与用户的中介模型
    user = models.ForeignKey(User)
    notice = models.ForeignKey(Notice)
    is_send = models.BooleanField(default=False) #这条消息是否被该用户通过websocket读到

