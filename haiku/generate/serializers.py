from rest_framework import serializers
from generate.models import Generation


class GenerateSerializer(serializers.Serializer):
    created = serializers.CharField(required=False, default='', max_length=100)

    def create(self, validated_data):
        return Generation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
