from rest_framework import serializers


class PhotoSerializer(serializers.Serializer):
    image = serializers.ImageField()


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField()

    def validate_phone(self, phone):
        if phone.startswith('7') is False or len(phone) != 11:
            raise serializers.ValidationError("Phone must be a `79999999999` string")
