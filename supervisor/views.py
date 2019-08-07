# -*- coding: utf-8 -*-
from rest_framework import viewsets

from django.shortcuts import render
from .models import Supervisor

from .serialiser import SupervisorsSerialiser
# Create your views here.

class ContainersViewSet(viewsets.ModelViewSet):

    queryset = Supervisor.objects.all()
    serializer_class = SupervisorsSerialiser