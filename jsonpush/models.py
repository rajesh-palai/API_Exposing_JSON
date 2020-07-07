from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from timezone_field import TimeZoneField


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="userInfo_by_user")
    ok = models.BooleanField(default=True)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="members")
    member_id = models.CharField(max_length=30)
    real_name = models.CharField(max_length=30,null=True)
   # tz = TimeZoneField(null=True)
    tz = models.CharField(max_length=30,null=True)


    def __str__(self):
        return self.real_name



class ActivityPeriods(models.Model):
    member = models.ForeignKey(UserProfile,on_delete= models.DO_NOTHING,related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# Create your models here.
