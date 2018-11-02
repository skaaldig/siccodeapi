from rest_framework import serializers
from . import models


class IndustrySectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IndustrySector
        fields = ['url', 'industry_sector', 'description']


class IndustryGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IndustryGroup
        fields = ['url', 'industry_group', 'description']


class IndustrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Industry
        fields = ['url', 'industry', 'description']


class SicCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SicCode
        fields = [
            'url', 'industry_sector',
            'industry_group', 'industry',
            'sic_code', 'description'
        ]
