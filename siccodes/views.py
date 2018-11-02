from rest_framework import viewsets
from . import models
from . import serializers


class IndustrySectorViewSet(viewsets.ModelViewSet):
    queryset = models.IndustrySector.objects.all()
    serializer_class = serializers.IndustrySectorSerializer
    filter_fields = ('sector_id',)


class IndustryGroupViewSet(viewsets.ModelViewSet):
    queryset = models.IndustryGroup.objects.all()
    serializer_class = serializers.IndustryGroupSerializer
    filter_fields = ('group_id', 'sector_id')


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = models.Industry.objects.all()
    serializer_class = serializers.IndustrySerializer
    filter_fields = ('industry_id', 'group_id')


class SicCodeViewSet(viewsets.ModelViewSet):
    queryset = models.SicCode.objects.all()
    serializer_class = serializers.SicCodeSerializer
    filter_fields = ('sic_code',)
