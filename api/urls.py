from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    
    
    path('fishtypes/', views.FishTypeListCreateView.as_view(), name='fishtype-list-create'),
    path('fishtypes/list/', views.FishTypeListView.as_view(), name='fishtype-list'),
    path('fishtypes/<int:pk>/', views.delete_fish_type, name='delete_fish_type'),
    
    path('weighin/', views.WeighInCreateView.as_view(), name='weighin-create'),
    path('weighins-list/', views.WeighInListAPIView.as_view(), name='weighin-list'),
    
    path('fish-totals/', views.FishTotalKilosView.as_view(), name='fish_totals'),
]