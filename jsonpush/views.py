from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ActivityPeriodsSerializers,UserProfileSerializers,UserInfoSerializers,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User

def index(request):

    return render(request,'jsonpush/index.html')


class UserListDetailsView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserRetrieveDeleteUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'



