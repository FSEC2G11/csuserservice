from rest_framework import serializers
from .models import CDAUsers

class CDAUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CDAUsers
        fields = ['username', 'firstname', 'lastname', 'usertype', 'email', 'password']
        