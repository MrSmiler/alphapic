
from rest_framework import serializers
from home.models import User


# this class is for converting User information to a format suitable for
# transfering user data
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                'username', 'email','birth_date'] 






