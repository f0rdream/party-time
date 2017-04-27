//创建一个socket对象,path名字为日程所在的群组名字
socket = new WebSocket("ws://" + window.location.host + "/tianxing/");

//接收数据函数
//有以下数据
//1.data.sender,data.groupname,data.text,data.time,data.mid,data.time
socket.onmessage = function(message) {
   var data = JSON.parse(message.data);
   alert("你的小组"+data.groupname+"\n"+data.sender
   +"\n"+data.text+"\n"+data.time+"\n"+data.m_id)
//设置已经接到通知的后台操作
//   notice = Notice.objects.get(id=m_id)//从后台拿到Message对象
//   membership = Membership.objects.get(notice=notice,user=user)//user为接受消息的用户
//   membership.is_send=True
//   membership.save()
}

//发送数据函数
socket.onopen = function() {
    //发送方的发送数据
    var a = {
        sender:"tang",//发送者的用户名字
        text:"text", //三种情况,1.退群通知,2.进群通知,3.添加日程通知
        groupname:"tianxing",//日程所在的小组名字
      }
     socket.send(JSON.stringify(a));
}

// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();

//退群时断开websocket

//接收不在线时的通知
//通过notice.sendname,notice.groupname,notice.text创造消息
//for m in user.membership_set.filter(is_send=False):
//    print(m.notice.time,m.notice.sender,m.notice.groupname)





