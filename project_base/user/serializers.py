from rest_framework import serializers

from user.models import User


class UserUpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if validated_data.get('image'):
            instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'image']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100, required=True, style={'input_type': 'password'})
    new_password = serializers.CharField(max_length=100, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['old_password', 'new_password']
        extra_kwargs = {
            'old_password': {
                'write_only': True,
            },
            'new_password': {
                'write_only': True,
            },
        }
