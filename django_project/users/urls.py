from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path("users/", views.getusers.as_view(), name="listusers"),
    path("users/<pk>/", views.editusers.as_view(), name="editusers"),
    path('users/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
