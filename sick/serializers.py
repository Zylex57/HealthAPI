from rest_framework import serializers
from sick.models import Sick


class SickListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sick
        fields = ('id', 'name', 'user')


class SickDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sick
        fields = '__all__'
