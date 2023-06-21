from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from .models import Member
from .serializer import MemberSerializer
# Create your views here.

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer