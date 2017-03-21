import datetime
from django.contrib.auth.models import User
from tasks.models import Task
from django.utils.timezone import datetime as dt

def get_count(obj, hour,day):
    group_name = obj.name
    users = User.objects.filter(groups__name=group_name)
    day = datetime.date.today()+datetime.timedelta(days=day)
    print day
    count = 0
    start_time = datetime.time(second=0, hour=hour, minute=0)
    end_time = datetime.time(hour=hour+2, minute=0, second=0)
    start = dt.combine(day, start_time)
    end = dt.combine(day, end_time)
    print start
    for user in users:
        tasks_start = Task.objects.filter(user=user, start_time__range=(start, end))
        tasks_end = \
            Task.objects.exclude(user=user,
                                 start_time__range=(start, end)).filter(user=user,
                                                                        end_time__range=(start, end))
        print tasks_end
        count += tasks_start.count() + tasks_end.count()
    return count

