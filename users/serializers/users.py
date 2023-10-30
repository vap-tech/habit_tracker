from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ User serializer """
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'patronymic', 'phone', 'city',)
