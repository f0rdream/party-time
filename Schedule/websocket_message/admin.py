from django.contrib import admin
from .models import Notice, Membership


class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ["sender", "groupname", "text", "time"]

    class Meta:
        model = Notice


class MembershipModelAdmin(admin.ModelAdmin):
    list_display = ["user", "notice", "is_send"]

    class Meta:
        model = Membership


admin.site.register(Notice, NoticeModelAdmin)
admin.site.register(Membership, MembershipModelAdmin)
# Register your models here.
