from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from common import models
from ..serializers import serializers_event
# Create your views here.

class Club_eventViewset(viewsets.ModelViewSet):
    queryset = models.ClubEvents.objects.all()
    serializer_class = serializers_event.Club_eventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['club']
   