import datetime

from django.utils import timezone
from rest_framework import serializers
from .models import Version, Chek_update


class UpdaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ("github_path", "timestamp", "version", "enable")

class Check_updateSerializer(serializers.Serializer):
    call = serializers.CharField(max_length=10)
    timestamp = serializers.DateTimeField(read_only=True)
    version = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Chek_update.objects.create(**validated_data)

    def delete(self, instance):
        return instance.delete()
