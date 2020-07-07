from .models import *
from rest_framework.serializers import ModelSerializer


class ActivityPeriodsSerializers(ModelSerializer):

    class Meta:
        model = ActivityPeriods
        #fields="__all__"
        exclude = ['id','member']



class UserProfileSerializers(ModelSerializer):
    activity_periods = ActivityPeriodsSerializers(many=True)

    class Meta:
        model = UserProfile
        #fields="__all__"
        exclude = ['id','user']



class UserInfoSerializers(ModelSerializer):
    #members = UserProfileSerializers(many=True)

    class Meta:
        model = UserInfo
        #fields="__all__"
        exclude = ['id','user']


class UserSerializer(ModelSerializer):
    userInfo_by_user = UserInfoSerializers()
    members = UserProfileSerializers(many=True)


    class Meta:
        model = User
        fields=["userInfo_by_user","members"]



