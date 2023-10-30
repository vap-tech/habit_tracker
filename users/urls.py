from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views.users import UserCreateView

from users.views.jwt import MyTokenObtainPairView

app_name = UsersConfig.name

urlpatterns = [
    path('create-user/', UserCreateView.as_view()),
    path('get-token/', MyTokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
]
