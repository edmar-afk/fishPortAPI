from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FishType, WeighIn, FishingPermit

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'is_superuser']
        extra_kwargs = {'is_superuser': {'read_only': True}}  # Prevents `is_superuser` from being set via the API

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            is_superuser=False  # Set default value for is_superuser
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
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
        

class FishingPermitSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)  # Accepts the owner ID
    
    class Meta:
        model = FishingPermit
        fields = [
            'owner', 'owner_name', 'address', 'home_port', 'vessel_name', 'vessel_type', 
            'color', 'service_type', 'vessel_description', 'length', 'breadth', 'depth', 
            'draught', 'gross', 'net', 'engine', 'serial_num', 'horse_power', 'cylinder_num', 
            'engine_num', 'crew_num', 'coast_guard_num', 'mfvr_num', 'or_num', 'date_issued', 'amount', 'fishing_gear_used'
        ]
        read_only_fields = ['id']  # Make only the `id` field read-only

