from rest_framework import serializers


class PhotoSerializer(serializers.Serializer):
    image = serializers.ImageField()