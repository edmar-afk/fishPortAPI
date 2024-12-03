from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('user/', views.UserDetailView.as_view(), name='user_detail'),
    
    path('fishtypes/', views.FishTypeListCreateView.as_view(), name='fishtype-list-create'),
    path('fishtypes/list/', views.FishTypeListView.as_view(), name='fishtype-list'),
    path('fishtypes/<int:pk>/', views.delete_fish_type, name='delete_fish_type'),
    
    path('weighin/', views.WeighInCreateView.as_view(), name='weighin-create'),
    path('weighins-list/', views.WeighInListAPIView.as_view(), name='weighin-list'),
    
    path('fish-totals/', views.FishTotalKilosView.as_view(), name='fish_totals'),
    
    path('register-fishing-permit/<int:user_id>/', views.FishingPermitCreateAPIView.as_view(), name='register-fishing_permit'),
    path('fishing-permit/latest/<int:userId>/', views.LatestFishingPermitAPIView.as_view(), name='latest_fishing_permit'),
    
    path('non-superuser-count/', views.NonSuperUserCountAPIView.as_view(), name='non-superuser-count'),
    path('fishermen/', views.FishermanListView.as_view(), name='fishermen-list'),
    path('fishing-permits/latest/<int:userId>/', views.LatestFishingPermitAPIView.as_view(), name='latest-fishing-permit'),
    path('fishing-permit/<int:userId>/', views.FishingPermitDetailsView.as_view(), name='fishing-permit-details'),
    
    path('total-weight-today/', views.TotalWeightTodayView.as_view(), name='total_weight_for_today'),
    path('total-price-today/', views.TotalPriceTodayView.as_view(), name='total-price-today'),
    
    
    path('weighin/<str:fish_name>/<str:dateWeighin>/', views.WeighInByFishView.as_view(), name='weighin-by-fish'),


    path('users/delete/<int:id>/', views.UserDeleteView.as_view(), name='user-delete'),
    
    
    path('vessel-registration/<int:user_id>/', views.VesselRegistrationCreateAPIView.as_view(), name='vessel-registration-create'),
    path('vessel-registration/latest/<int:userId>/', views.LatestVesselRegAPIView.as_view(), name='latest-vessel-registration'),
    path('vessel-registrationDetail/<int:vesselId>/', views.VesselRegistrationDetailsView.as_view(), name='vessel-registration-details'),

    path('fishing-permits/<int:permitId>/grant/', views.GrantFishingPermitView.as_view(), name='grant-fishing-permit'),
    path('vessel-registration/<int:vesselId>/grant/', views.GrantVesselRegView.as_view(), name='grant-vessel-registration'),
    
    path('permit/status/<int:ownerId>/', views.FishingPermitStatusView.as_view(), name='permit-status'),
    path('vessel/status/<int:ownerId>/', views.VesselRegistrationStatusView.as_view(), name='vessel-status'),
    
    path('fishing-permit-income/', views.TotalAmountGrantedFishingPermits.as_view(), name='fishing-permit-income'),
    path('vessel-registration-income/', views.TotalAmountGrantedVesselRegistrations.as_view(), name='vessel-registration-income'),
    
    
    path("fishing-permits/<int:permit_id>/docx/", views.download_fishing_permit, name="download_fishing_permit"),
    
    path('vessel-registrations/<int:owner_id>/', views.VesselRegistrationListByOwner.as_view(), name='vessel-registrations-by-owner'),

    path('users/<int:userId>/', views.UserProfileView.as_view(), name='user-detail'),
    path('users/<int:userId>/edit/', views.UserProfileUpdateView.as_view(), name='user-edit'),


    path('upload-expiration-date/<int:vesselid>/', views.ExpirationDateUploadView.as_view(), name='upload-expiration-date'),
    path('expiration-dates/<int:vessel_id>/', views.ExpirationDateByVesselIdView.as_view(), name='expiration-dates-by-vessel-id'),
    
    path('permit-expiration/<int:permitid>/', views.PermitExpirationDateUploadView.as_view(), name='permit-expiration-upload'),
    path('permit-expiration-dates/<int:permit_id>/', views.ExpirationDateByPermitIdView.as_view(), name='permit-expiration-dates'),
    
    path('users/granted-status/', views.GrantedUsersView.as_view(), name='user-granted-status'),
]
