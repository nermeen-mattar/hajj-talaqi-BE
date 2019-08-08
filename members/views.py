# -*- coding: utf-8 -*-
from rest_framework import viewsets

from django.shortcuts import render
from .models import Member

from .serialiser import MembersSerialiser
# Create your views here.

class MembersViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        office = self.kwargs['office_id']
        return Member.objects.filter(office = office)

    queryset = Member.objects.all().order_by("-created_at")
    serializer_class = MembersSerialiser