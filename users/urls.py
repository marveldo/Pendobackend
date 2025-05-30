from django.urls import path
from .views import CustomTokenObtainPairView, UserView , CustomTokenRefreshView

urlpatterns = [
    path('login/',CustomTokenObtainPairView.as_view()),
    path('refresh/', CustomTokenRefreshView.as_view()),
    path('', UserView.as_view() )
]