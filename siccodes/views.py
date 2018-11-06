from rest_framework import viewsets
from . import models
from . import serializers


class IndustrySectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.IndustrySector.objects.all()
    serializer_class = serializers.IndustrySectorSerializer
    filter_fields = ('sector_id', 'description')


class IndustryGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.IndustryGroup.objects.all()
    serializer_class = serializers.IndustryGroupSerializer
    filter_fields = ('group_id', 'sector_id', 'description')


class IndustryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Industry.objects.all()
    serializer_class = serializers.IndustrySerializer
    filter_fields = ('industry_id', 'group_id', 'description')


class SicCodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SicCode.objects.all()
    serializer_class = serializers.SicCodeSerializer
    filter_fields = ('sic_code', 'description')
