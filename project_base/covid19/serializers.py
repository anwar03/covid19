from datetime import datetime
from rest_framework import serializers
from .models import Covid
from contact.serializers import CountrySerializer


class Covid19Serializer(serializers.ModelSerializer):

    class Meta:
        model = Covid
        fields = ['id', 'country', 'confirmed', 'death', 'recovered', 'created_at', 'latitude', 'longitude']

    def create(self, validated_data):
        covid19 = self.Meta.model.objects.create(**validated_data)
        return covid19

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country', instance.country)
        instance.confirmed = validated_data.get('confirmed', instance.confirmed)
        instance.death = validated_data.get('death', instance.death)
        instance.recovered = validated_data.get('recovered', instance.recovered)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()

        return instance

    def validate_created_at(self, value):
        try:
            value = value.strftime('%Y-%m-%d')
            return value
        except ValueError:
            return False
