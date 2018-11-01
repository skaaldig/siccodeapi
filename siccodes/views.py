from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers


class MajorGroupViewSet(viewsets.ModelViewSet):
    queryset = models.MajorGroup.objects.all()
    serializer_class = serializers.MajorGroupSerializer


class IndustryGroupViewSet(viewsets.ModelViewSet):
    queryset = models.IndustryGroup.objects.all()
    serializer_class = serializers.IndustryGroupSerializer


class IndustrySectorViewSet(viewsets.ModelViewSet):
    queryset = models.IndustrySector.objects.all()
    serializer_class = serializers.IndustrySectorSerializer


class SicCodeViewSet(viewsets.ModelViewSet):
    queryset = models.SicCode.objects.all()
    serializer_class = serializers.SicCodeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sic_code',)
