from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers.jwt import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """ Token obtain endpoint """
    serializer_class = MyTokenObtainPairSerializer
