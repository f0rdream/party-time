# coding:utf-8
import requests
import urllib
import urllib2
import hashlib
from bs4 import BeautifulSoup as bs
from .models import Course
import datetime
from django.contrib.auth.models import User
import sys
from tasks.models import Task
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
def get_start_time(number):
    if number == "1":
        return "08:00:00Z"
    if number == "2":
        return "08:50:00Z"
    if number == "3":
        return "09:50:00Z"
    if number == "4":
        return "10:40:00Z"
    if number == "5":
        return "11:30:00Z"
    if number == "6":
        return "14:05:00Z"
    if number == "7":
        return "14:55:00Z"
    if number == "8":
        return "15:45:00Z"
    if number == "9":
        return "16:40:00Z"
    if number == "10":
        return "17:30:00Z"
    if number == "11":
        return "18:30:00Z"
    if number == "12":
        return "19:20:00Z"
    if number == "13":
        return "20:10:00Z"
def get_end_time(number):
    if number == "1":
        return "08:45:00Z"
    if number == "2":
        return "09:35:00Z"
    if number == "3":
        return "10:35:00Z"
    if number == "4":
        return "11:25:00Z"
    if number == "5":
        return "12:15:00Z"
    if number == "6":
        return "14:50:00Z"
    if number == "7":
        return "15:40:00Z"
    if number == "8":
        return "16:30:00Z"
    if number == "9":
        return "17:25:00Z"
    if number == "10":
        return "18:05:00Z"
    if number == "11":
        return "19:15:00Z"
    if number == "12":
        return "20:05:00Z"
    if number == "13":
        return "20:55:00Z"
def get_date(day):
    now_day = datetime.datetime.now().weekday()
    course_day = 0
    if day == "周一":
        course_day = 0
    if day == "周二":
        course_day = 1
    if day == "周三":
        course_day = 2
    if day == "周四":
        course_day = 3
    if day == "周五":
        course_day = 4
    if day == "周六":
        course_day = 5
    if day == "周日":
        course_day = 6
    course_date = datetime.datetime.now().date()+(course_day-now_day)*datetime.timedelta(days=1)
    return course_date



def spider(user,login_id,login_pwd,yzm_text,yzm_cookie):
    if len(Course.objects.all()) != 0:
        for course in Course.objects.all():
            course.delete()
            print "delete success"
    if len(Task.objects.filter(is_course=True))!=0:
        for task in Task.objects.filter(is_course=True):
            task.delete()
            print "delete success"
    home_url = 'http://210.42.121.241'
    login_url = 'http://210.42.121.241/servlet/Login'
    image_url = 'http://210.42.121.241/servlet/GenImg'
    login_pwd = hashlib.md5(login_pwd).hexdigest()
    data = urllib.urlencode({
        'id': login_id,
        'pwd': login_pwd,
        'xdvfb': yzm_text
    })

    req = urllib2.Request(login_url, data, headers={'Cookie': yzm_cookie})
    content = urllib2.urlopen(req).read()

    soup = bs(content, "lxml")
    namediv = soup.find_all(attrs={'id': 'nameLable'})
    termspan = soup.find_all(attrs={'id': 'term'})

    stu_name = ''
    stu_term = ''

    for name in namediv:
        stu_name = name.text.encode('utf-8').lstrip().rstrip()
    for term in termspan:
        stu_term = term.text.encode('utf-8').lstrip().rstrip()
    table_url = 'http://210.42.121.241/stu/stu_course_parent.jsp'
    requset = urllib2.Request(table_url, headers={'Cookie': yzm_cookie})
    class_table = urllib2.urlopen(requset).read()
    tsoup = bs(class_table, 'lxml')
    page_iframe = tsoup.find_all(attrs={'id': 'iframe0'})
    page_url = ''
    for page in page_iframe:
        page_url = home_url + page.get('src')[:-8] + "%CF%C2&state="
    requset = urllib2.Request(page_url, headers={'Cookie': yzm_cookie})
    table_content = urllib2.urlopen(requset).read()


    csoup = bs(table_content, 'lxml')
    listTable = csoup.find_all(attrs={'class': 'table listTable'})
    tr = listTable[0].find_all('tr')
    tr_num = len(tr)
    for i in range(1, tr_num):
        td = tr[i].find_all('td')
        course_num = td[0].text.encode("utf-8").strip()
        course_name = td[1].text.encode("utf-8").strip()
        course_type = td[2].text.encode("utf-8").strip()
        course_college = td[4].text.encode("utf-8").strip()
        course_teacher = td[5].text.encode("utf-8").strip()
        course_major = td[6].text.encode("utf-8").strip()
        course_point = td[7].text.encode("utf-8").strip()
        course_time = td[9].text.encode("utf-8").strip()
        time_dict = course_time.split(":")
        day = time_dict[0]
        class_num = time_dict[1].split(";")[1].split("节")[0].split("-")
        start_num = class_num[0].split("\n")[1]
        end_num = class_num[1]
        try:
            Course.objects.create(user=user,stu_name=stu_name,stu_term=stu_term,
                             course_num=course_num,course_name=course_name,course_type=course_type,
                             course_college=course_college,course_teacher=course_teacher,course_major=course_major,
                             course_point=course_point,day=day,start_num=start_num,end_num=end_num)
            print day
            date = get_date(day)
            print "get the date"
            start_time = str(date) +"T" + get_start_time(start_num)
            end_time = str(date) +"T"+get_end_time(end_num)

            title = course_name
            detail = ""
            print title
            print start_time
            print end_time
            task =Task.objects.create(user=user,title=title,detail=detail,start_time=start_time,end_time=end_time,
                                is_course=True,day=day,start_num=start_num,end_num=end_num)
            task.save()
        except  Exception as e:
            print e,e.message
def save_img(username,yzm_image):
    yzm_file =  'media_root/yzm/'+str(username) + ".jpg"
    with open(yzm_file, 'wb') as f:
        f.write(yzm_image)
