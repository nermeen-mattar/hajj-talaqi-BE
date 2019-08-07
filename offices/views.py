# -*- coding: utf-8 -*-
from rest_framework import viewsets

from django.shortcuts import render
from .models import Office

from .serialiser import OfficesSerialiser
# Create your views here.

class OfficesViewSet(viewsets.ModelViewSet):

    queryset = Office.objects.all()
    serializer_class = OfficesSerialiser