from rest_framework import serializers


class PointSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    def to_representation(self, instance):
        return {
            "type": "Feature",
            "id": instance['id'],
            "geometry": {
                "type": "Point",
                "coordinates": [instance['latitude'], instance['longitude']],
            }
        }
