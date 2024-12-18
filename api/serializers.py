from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FishType, WeighIn, FishingPermit, VesselRegistration, ExpirationDate, PermitExpirationDate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'is_superuser', 'date_joined']
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
            'id', 'owner', 'owner_name', 'address', 'home_port', 'vessel_name', 'vessel_type', 
            'color', 'service_type', 'vessel_description', 'length', 'breadth', 'depth', 
            'draught', 'gross', 'net', 'engine', 'serial_num', 'horse_power', 'cylinder_num', 
            'engine_num', 'crew_num', 'coast_guard_num', 'mfvr_num', 'or_num', 'date_issued', 'amount', 'fishing_gear_used', 'status'
        ]
        read_only_fields = ['id']  # Make only the `id` field read-only



class VesselRegistrationSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)  # Accepts the owner ID
    
    class Meta:
        model = VesselRegistration
        fields = [
            'id',
            'owner',
            'vessel_name',
            'service_type',
            'home_port',
            'builder_name',
            'year_built',
            'place_built',
            'former_vessel_name',
            'former_owner',
            'hull_materials',
            'color',
            'length',
            'width',
            'depth',
            'draught',
            'gross_tonnage',
            'net_tonnage',
            'engine_make',
            'cycle',
            'horsepower',
            'cylinder_number',
            'number_of_engine',
            'status',
            'amount',
        ]
        read_only_fields = ['id']  # To ensure the ID is read-only
        
        
class ExpirationDateSerializer(serializers.ModelSerializer):
    vessel_reg = VesselRegistration()

    class Meta:
        model = ExpirationDate
        fields = ['id', 'vessel_reg', 'date_registered', 'date_expired']
       

class PermitExpirationDateSerializer(serializers.ModelSerializer):
    permit_reg = FishingPermitSerializer()  # Assuming you have a `FishingPermitSerializer`

    class Meta:
        model = PermitExpirationDate
        fields = ['id', 'permit_reg', 'date_registered', 'date_expired']

       
