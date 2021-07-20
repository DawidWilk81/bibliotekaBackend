from rest_framework import serializers
from .models import Ksiazka
from django.contrib.auth.models import User


class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = ['id', 'tytul', 'autor', 'zdjecie', 'uzytkownik']

class KsiazkaSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = ['id', 'tytul', 'autor', 'zdjecie', 'uzytkownik']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user




