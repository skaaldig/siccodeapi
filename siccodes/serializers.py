from rest_framework import serializers
from . import models


class IndustrySectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IndustrySector
        fields = ['url', 'sector_id', 'description']


class IndustryGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IndustryGroup
        fields = ['url', 'group_id', 'description']


class IndustrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Industry
        fields = ['url', 'industry_id', 'description']


class SicCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SicCode
        fields = [
            'url', 'sector_id',
            'group_id', 'industry_id',
            'sic_code', 'description'
        ]
