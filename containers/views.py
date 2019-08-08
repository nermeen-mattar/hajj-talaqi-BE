# -*- coding: utf-8 -*-
from rest_framework import viewsets

from django.shortcuts import render
from .models import Container

from .serialiser import ContainersSerialiser
# Create your views here.

class ContainersViewSet(viewsets.ModelViewSet):

    queryset = Container.objects.all().order_by("-created_at")
    serializer_class = ContainersSerialiser