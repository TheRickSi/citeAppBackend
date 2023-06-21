from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
from .permissions import *

from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CiteViewset(viewsets.ModelViewSet):
    serializer_class = CiteSerializer
    queryset = Cite.objects.all()
    pagination_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner','id']
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
