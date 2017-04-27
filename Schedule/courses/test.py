# coding:utf-8
import time,datetime
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
    print course_date
get_date("周三")




