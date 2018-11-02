from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers


class IndustrySectorViewSet(viewsets.ModelViewSet):
    queryset = models.IndustrySector.objects.all()
    serializer_class = serializers.IndustrySectorSerializer


class IndustryGroupViewSet(viewsets.ModelViewSet):
    queryset = models.IndustryGroup.objects.all()
    serializer_class = serializers.IndustryGroupSerializer


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = models.Industry.objects.all()
    serializer_class = serializers.IndustrySerializer


class SicCodeViewSet(viewsets.ModelViewSet):
    queryset = models.SicCode.objects.all()
    serializer_class = serializers.SicCodeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sic_code',)
