from django.urls import path
from .views import CustomTokenObtainPairView, UserView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('login/',CustomTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('', UserView.as_view() )
]