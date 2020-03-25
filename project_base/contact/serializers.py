from rest_framework import serializers

from contact.models import Contact, Address, Country


class ContactSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        contact = self.Meta.model.objects.create(**validated_data)
        return contact

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.save()

        return instance

    class Meta:
        model = Contact
        fields = ['id', 'email', 'mobile', 'telephone']


class AddressSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        address = self.Meta.model.objects.create(**validated_data)
        return address

    def update(self, instance, validated_data):
        instance.line1 = validated_data.get('line1', instance.line1)
        instance.line2 = validated_data.get('line2', instance.line2)
        instance.zip = validated_data.get('zip', instance.zip)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        country = validated_data.get('country', instance.country)
        if type(country) is int:
            country = Country.objects.get(id=country)
        instance.country = country
        instance.save()

        return instance

    class Meta:
        model = Address
        fields = ['id', 'line1', 'line2', 'zip', 'state', 'city', 'country']
