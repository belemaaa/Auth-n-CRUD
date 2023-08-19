from rest_framework import serializers
from .models import Post


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'content']