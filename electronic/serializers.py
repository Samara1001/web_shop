from rest_framework import serializers
from .models import Electronic


class ElectronicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Electronic
        fields = '__all__'

