# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
import datetime
from django.db.models.signals import pre_save

class Task(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=False, default='', editable=True)
    detail = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()  # 开始时间
    end_time = models.DateTimeField()  # 结束时间
    # slug = models.SlugField(unique=True)
    # start_week = models.IntegerField(null=True, blank=True, choices=WEEK_CHOICES) # 开始周
    # end_week = models.IntegerField(null=True, blank=True, choices=WEEK_CHOICES) # 结束周
    # period_week = models.IntegerField(blank=True, null=True) # 持续周数
    # period_time = models.IntegerField(default=0) # 持续课时
    # day = models.CharField(choices=DAY_CHOICES,blank=True) # 星期

    def save(self, *args, **kwargs):
        if self.start_time < self.end_time:
            super(Task, self).save(*args, **kwargs)
        elif self.start_time >= self.end_time:
            self.end_time = self.start_time + datetime.timedelta(1)
            super(Task, self).save(*args, **kwargs)




    def get_absolute_url(self):
        return reverse("tasks:detail", kwargs={'title': self.title})

    # def get_absolute_url(self):
    #     return reverse("tasks:detail", kwargs={'title': self.title})

    def get_seconds(self):
        return (self.end_time-self.start_time).total_seconds()

    def __unicode__(self):
        return self.title


# def create_slug(instance, created_slug=None):
#     slug = slugify(instance.title)
#     if created_slug is not None:
#         slug = created_slug
#     query = Task.objects.filter(slug=slug).order_by('id')
#     if query.exists():
#         new_slug = "%s-%s" %(slug, query.first().id)
#         return created_slug(instance, created_slug=new_slug)
#     return slug
#
#
# def pre_save_task_receiver(sender, instance,*args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
# pre_save.connect(pre_save_task_receiver,sender=Task)





# Create your models here.
