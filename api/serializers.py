from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FishType, WeighIn

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class FishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishType
        fields = ['id', 'name']

class WeighInSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = WeighIn
        fields = ['id', 'fish', 'price_per_kilo', 'kg', 'total_price', 'date_weighin']
        read_only_fields = ['date_weighin']


class WeighInHistorySerializer(serializers.ModelSerializer):
    fish = FishTypeSerializer()  # Use the FishTypeSerializer to include fish details

    class Meta:
        model = WeighIn
        fields = ['id', 'fish', 'price_per_kilo', 'kg', 'total_price', 'date_weighin']
        read_only_fields = ['date_weighin']

class FishCaugthReportSerializer(serializers.ModelSerializer):
    fish = FishTypeSerializer()  # Use the FishTypeSerializer to include fish details
    class Meta:
        model = WeighIn
        fields = ['fish', 'kg']