#coding:UTF-8
from channels import Group
from channels.auth import channel_session_user_from_http,channel_session,channel_session_user
from .models import Notice,Membership
import json
from django.contrib.auth.models import User
from django.contrib.auth.models import Group as DGroup #为了跟Channels的Group区别
#连接到websocket.connect

@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    room = message.content['path'].strip('/')
    message.channel_session['room'] = room
    Group("chat-%s" % room).add(message.reply_channel)

#连接到websocket.receive
@channel_session_user
def ws_message(message):
    room = message.channel_session['room']#路径就是组名
    g = DGroup.objects.get(name=room)#拿到对应的Group对象
    data = json.loads(message['text'])#从前端拿到的json数据
    notice = Notice.objects.create(sender=data['sender'],groupname=data['groupname'],
                               text=data['text'])
    #创建多对多的关系
    for user in g.user_set.all():
        Membership.objects.create(user=user,notice=notice,is_send=False)
    Group("chat-%s" % room).send({
        'text':json.dumps({
            'sender':data['sender'],
            'text':data['text'],
            'groupname':data['groupname'],
            'time':notice.time.strftime('%b %-d %-I:%M %p'),
            'm_id':notice.id,
        }
      )
    })

@channel_session_user_from_http
def ws_disconnect(message):
    room = message.channel_session['room']
    Group("chat-%s" % room).discard(message.reply_channel)
