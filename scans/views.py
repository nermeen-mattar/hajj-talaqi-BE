# -*- coding: utf-8 -*-
from rest_framework import viewsets

from django.shortcuts import render
from .models import Scan

from .serialiser import ScansSerialiser
# Create your views here.

class ScansViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        office = self.kwargs['office_id']
        return Scan.objects.filter(office = office)
    queryset = Scan.objects.all().order_by("-created_at")
    serializer_class = ScansSerialiser