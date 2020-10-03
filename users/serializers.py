from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200, write_only=True)
    bio = serializers.CharField(max_length=1000, default="There is no bio yet!")
    first_name = serializers.CharField(max_length=25, default="")
    last_name = serializers.CharField(max_length=25, default="")
    email = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username= validated_data.get('username', instance.username)
        instance.email= validated_data.get('email', instance.email)
        instance.bio= validated_data.get('bio', instance.bio)
        instance.save()
        return instance
    
    class Meta:
        model = CustomUser
        # fields = ('id', 'username', 'email', 'password')