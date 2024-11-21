# views.py
from rest_framework import generics, permissions, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserSerializer, FishTypeSerializer, WeighInSerializer, WeighInHistorySerializer, VesselRegistrationSerializer, FishingPermitSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.decorators import api_view
from .models import FishType, WeighIn, FishingPermit, VesselRegistration
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
import logging
from rest_framework.decorators import permission_classes
logger = logging.getLogger(__name__)
from datetime import timedelta
from django.db.models import Count  # Import Count for aggregation
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, NotFound  # Import exceptions

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        # Print the incoming request data to the console
        print("Received data:", request.data)

        # Continue with your serializer logic
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If there are errors, print them too
        print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FishTypeListCreateView(generics.ListCreateAPIView):
    queryset = FishType.objects.all()
    serializer_class = FishTypeSerializer
    permission_classes = [AllowAny]


# New view for listing FishTypes only
class FishTypeListView(generics.ListAPIView):
    queryset = FishType.objects.all()
    serializer_class = FishTypeSerializer
    permission_classes = [AllowAny]

# New view for listing FishTypes only
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_fish_type(request, pk):
    try:
        fish_type = FishType.objects.get(pk=pk)
    except FishType.DoesNotExist:
        return Response({'error': 'Fish type not found.'}, status=status.HTTP_404_NOT_FOUND)

    fish_type.delete()
    return Response({'message': 'Fish type deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

class WeighInCreateView(generics.CreateAPIView):
    queryset = WeighIn.objects.all()
    serializer_class = WeighInSerializer
    permission_classes = [AllowAny]

class WeighInListAPIView(generics.ListAPIView):
    queryset = WeighIn.objects.all()
    serializer_class = WeighInHistorySerializer
    permission_classes = [AllowAny]

class FishTotalKilosView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        # Get the current date
        today = timezone.now().date()

        # Filter weigh-ins for the current date and aggregate total kg per fish type
        fish_totals = (
            WeighIn.objects
            .filter(date_weighin__date=today)
            .values('fish')
            .annotate(total_kg=Sum('kg'))
            .order_by('fish')
        )

        # Prepare the response data
        response_data = []
        for item in fish_totals:
            fish_id = item['fish']
            total_kg = item['total_kg']
            fish_type = FishType.objects.get(id=fish_id)
            response_data.append({
                'fish': fish_type.name,
                'total_kg': total_kg
            })

        return Response(response_data, status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user




class NonSuperUserCountAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        # Count users who are not superusers
        non_superuser_count = User.objects.filter(is_superuser=False).count()
        return Response({'non_superuser_count': non_superuser_count})


class FishermanListView(generics.ListAPIView):
    permission_classes = [AllowAny]

    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

    def get_queryset(self):
        # Optionally, you can customize this method to filter the users
        return User.objects.filter(is_superuser=False)


class FishingPermitCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, user_id):
        # Retrieve the User object based on the provided user_id
        try:
            owner = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Include the owner object and set owner_name to user.first_name in the form data
        data = request.data.copy()
        data['owner'] = owner.id  # Set the owner to the user's ID
        data['owner_name'] = owner.first_name  # Automatically set owner_name to first_name

        # Print the submitted data for debugging
        print("Data being submitted:", data)

        # Serialize the data
        serializer = FishingPermitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Save the FishingPermit instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Print and return validation errors for debugging
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LatestFishingPermitAPIView(generics.RetrieveAPIView):
    serializer_class = FishingPermitSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        user_id = self.kwargs['userId']
        # Fetch the latest permit for the user if it exists
        return FishingPermit.objects.filter(owner_id=user_id).last()


class FishingPermitDetailsView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = FishingPermitSerializer

    def get_object(self):
        user_id = self.kwargs.get("userId")
        # Get the latest fishing permit for the user, ordered by ID in descending order
        permit = FishingPermit.objects.filter(owner__id=user_id).order_by('-id').first()
        if permit is None:
            self.raise_exception()  # Raise a 404 error if no permit is found
        return permit



class VesselRegistrationCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, user_id):
        # Retrieve the User object based on the provided user_id
        try:
            owner = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Include the owner object in the form data
        data = request.data.copy()
        data['owner'] = owner.id  # Set the owner to the user's ID

        # Print the submitted data for debugging
        print("Data being submitted:", data)

        # Serialize the data
        serializer = VesselRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Save the VesselRegistration instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Print and return validation errors for debugging
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LatestVesselRegAPIView(generics.RetrieveAPIView):
    serializer_class = VesselRegistrationSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        user_id = self.kwargs['userId']
        # Fetch the latest permit for the user if it exists
        return VesselRegistration.objects.filter(owner_id=user_id).last()

class VesselRegistrationDetailsView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = VesselRegistrationSerializer

    def get_object(self):
        vessel_id = self.kwargs.get("vesselId")  # Extract `vesselId` from URL
        vessel = VesselRegistration.objects.filter(id=vessel_id).first()
        if vessel is None:
            raise NotFound("Vessel not found.")  # Use NotFound exception for 404
        return vessel



class TotalWeightTodayView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        today = now().date()  # Get the current date

        # Query WeighIn for today only and aggregate the total kg
        total_weight = WeighIn.objects.filter(
            date_weighin__date=today
        ).aggregate(total_weight=Sum('kg'))['total_weight'] or 0

        return Response({"total_weight_today": total_weight})


class TotalPriceTodayView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        today = now().date()  # Get the current date

        # Query WeighIn for today only and aggregate the total price
        total_price = WeighIn.objects.filter(
            date_weighin__date=today
        ).aggregate(total_price=Sum('total_price'))['total_price'] or 0

        return Response({"total_price_today": total_price})



class WeighInByFishView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        fish_name = self.kwargs['fish_name']
        current_date = timezone.now().date()

        try:
            fish = FishType.objects.get(name=fish_name)
        except FishType.DoesNotExist:
            raise NotFound(detail="Fish type not found.")

        weighin_queryset = WeighIn.objects.filter(fish=fish, date_weighin__date=current_date)
        total_kg = weighin_queryset.aggregate(total_kg=Sum('kg'))['total_kg'] or 0

        return Response({
            "fish_name": fish_name,
            "total_kg_today": total_kg
        })



class UserDeleteView(APIView):
    permission_classes = [AllowAny]
    """
    API view to delete a user based on their ID.
    """
    def delete(self, request, *args, **kwargs):
        # Retrieve the user ID from the URL
        user_id = kwargs.get('id')

        # Try to get the user object
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # Check if the user is allowed to delete (optional)
        # For example, prevent deleting superusers or the current authenticated user
        if user.is_superuser or user == request.user:
            return Response(
                {"detail": "You cannot delete this user."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Delete the user
        user.delete()
        return Response({"detail": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
class GrantFishingPermitView(APIView):
    permission_classes = [AllowAny]
    def patch(self, request, permitId):
        # Fetch the fishing permit object or return 404 if not found
        fishing_permit = get_object_or_404(FishingPermit, id=permitId)
        
        # Update the status field
        fishing_permit.status = 'Granted'
        fishing_permit.save()
        
        # Serialize the updated object
        serializer = FishingPermitSerializer(fishing_permit)
        
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GrantVesselRegView(APIView):
    permission_classes = [AllowAny]
    def patch(self, request, vesselId):
        # Fetch the fishing permit object or return 404 if not found
        vessel_registration = get_object_or_404(VesselRegistration, id=vesselId)
        
        # Update the status field
        vessel_registration.status = 'Granted'
        vessel_registration.save()
        
        # Serialize the updated object
        serializer = VesselRegistrationSerializer(vessel_registration)
        
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

class FishingPermitStatusView(APIView):
    permission_classes = [AllowAny]
    """
    API view to check the latest status of a fishing permit by ownerId.
    """
    def get(self, request, ownerId):
        # Validate that the owner exists
        owner = get_object_or_404(User, id=ownerId)

        # Fetch the latest permit for the given owner
        latest_permit = FishingPermit.objects.filter(owner=owner).order_by('-id').first()

        if latest_permit:
            return Response({
                "ownerId": ownerId,
                "owner_name": owner.get_full_name(),  # Assuming `get_full_name` exists
                "permit": {
                    "id": latest_permit.id,
                    "vessel_name": latest_permit.vessel_name,
                    "status": latest_permit.status,
                    "date_issued": latest_permit.date_issued,
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "ownerId": ownerId,
                "owner_name": owner.get_full_name(),
                "message": "No permits found for this owner."
            }, status=status.HTTP_404_NOT_FOUND)

            

class VesselRegistrationStatusView(APIView):
    permission_classes = [AllowAny]
    """
    API view to check the latest status of vessel registrations by ownerId.
    """
    def get(self, request, ownerId):
        # Validate that the owner exists
        owner = get_object_or_404(User, id=ownerId)

        # Fetch the latest vessel registration for the given owner
        latest_vessel = VesselRegistration.objects.filter(owner=owner).order_by('-id').first()

        if latest_vessel:
            return Response({
                "ownerId": ownerId,
                "owner_name": owner.get_full_name(),  # Assuming `get_full_name` exists
                "vessel": {
                    "id": latest_vessel.id,
                    "builder_name": latest_vessel.builder_name,
                    "year_built": latest_vessel.year_built,
                    "status": latest_vessel.status,
                    "amount": latest_vessel.amount,
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "ownerId": ownerId,
                "owner_name": owner.get_full_name(),
                "message": "No vessel registrations found for this owner."
            }, status=status.HTTP_404_NOT_FOUND)
            
            
class TotalAmountGrantedFishingPermits(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        # Filter fishing permits with status 'Granted' and sum the 'amount' field
        total_amount = FishingPermit.objects.filter(status='Granted').aggregate(total_amount=Sum('amount'))['total_amount']
        
        # If no permits are found with the 'Granted' status, set total_amount to 0
        if total_amount is None:
            total_amount = 0

        # Return the total amount in the response
        return Response({
            'total_amount_granted': total_amount
        }, status=status.HTTP_200_OK)
        
class TotalAmountGrantedVesselRegistrations(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        # Filter VesselRegistrations with status 'Active' and sum the 'amount' field
        total_amount = VesselRegistration.objects.filter(status='Granted').aggregate(total_amount=Sum('amount'))['total_amount']
        
        # If no registrations are found with the 'Active' status, set total_amount to 0
        if total_amount is None:
            total_amount = 0

        # Return the total amount in the response
        return Response({
            'total_amount_active': total_amount
        }, status=status.HTTP_200_OK)