from rest_framework import serializers
from .models import *


class HelloSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'id', 'password', 'balance', 'all_time_balance')
        extra_kwargs = {'password': {'write_only': True}, 'all_time_balance': {'read_only': True}}

    def create(self, validated_data):
        user = UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ('id', 'user_profile', 'created_on', 'waste', 'waste_desc')
        extra_kwargs = {'user_profile': {'read_only': True}}

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id', 'user_profile', 'balance')