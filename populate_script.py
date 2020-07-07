import os,django
import random
import string


os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Task1.settings')
django.setup()
from faker import Faker
from jsonpush.models import UserProfile,UserInfo,ActivityPeriods
from django.contrib.auth.models import User
from django.utils import timezone

def pre_populate(N,P):
    fake = Faker()
    for _ in range(N):
        id= random.randint(1,3)
        member_id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(8)])
        real_name = fake.name()
        tz = fake.country()
        user= User.objects.get(id=id)
        profile = UserProfile.objects.create(member_id= member_id,real_name=real_name,tz=tz,user = user)

        for _ in range(P):
            start_time = fake.date_time()
            end_time = fake.date_time()
            #ActivityPeriods.objects.create(start_time=start_time,end_time=end_time,member =UserProfile.objects.get(member_id=member_id) )
            ActivityPeriods.objects.create(start_time=start_time, end_time=end_time, member=profile)

pre_populate(20,3)





