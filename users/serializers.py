from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    profileimg = serializers.FileField()
    bio = serializers.CharField(max_length=1000, default="There is no bio yet!")
    first_name = serializers.CharField(max_length=25, default="")
    last_name = serializers.CharField(max_length=25, default="")
    email = serializers.CharField(max_length=50, default="")
    

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username= validated_data.get('username', instance.username)
        instance.email= validated_data.get('email', instance.email)
        instance.profileimg= validated_data.get('profileimg', instance.profileimg)
        instance.bio= validated_data.get('bio', instance.bio)
        instance.save()
        return instance