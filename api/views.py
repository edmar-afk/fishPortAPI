# views.py
from rest_framework import generics, permissions, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserSerializer, FishTypeSerializer, WeighInSerializer, WeighInHistorySerializer, FishCaugthReportSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.decorators import api_view
from .models import FishType, WeighIn
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class FishTypeListCreateView(generics.ListCreateAPIView):
    queryset = FishType.objects.all()
    serializer_class = FishTypeSerializer
    permission_classes = [AllowAny]
    

# New view for listing FishTypes only
class FishTypeListView(generics.ListAPIView):
    queryset = FishType.objects.all()
    serializer_class = FishTypeSerializer
    permission_classes = [AllowAny]
    
@api_view(['DELETE'])
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
                'fish': fish_type.name,  # or any other field from FishType
                'total_kg': total_kg
            })

        return Response(response_data, status=status.HTTP_200_OK)
    
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user