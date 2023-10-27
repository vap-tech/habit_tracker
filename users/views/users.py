from users.models import User
from rest_framework.generics import CreateAPIView

from users.serializers.users import UserSerializer


class UserCreateView(CreateAPIView):
    """ Create User """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()
