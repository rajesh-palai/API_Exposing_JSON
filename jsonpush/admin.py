from django.contrib import admin
from .models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user','ok' ]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'member_id','real_name','tz']


class ActivityPeriodsAdmin(admin.ModelAdmin):
    list_display = ['member', 'start_time','end_time']


admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(ActivityPeriods,ActivityPeriodsAdmin)

# Register your models here.
