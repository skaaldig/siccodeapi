from rest_framework import serializers
from .models import MajorGroup, IndustryGroup, IndustrySector, SicCode


class MajorGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MajorGroup
        fields = ['url', 'major_number', 'description']


class IndustryGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndustryGroup
        fields = ['url', 'major_number', 'description']


class IndustrySectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndustrySector
        fields = ['url', 'major_number', 'description']


class SicCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SicCode
        fields = [
            'url', 'major_group',
            'industry_group', 'industry_sector',
            'sic_code', 'description'
        ]
