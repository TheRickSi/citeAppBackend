from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields = '__all__'
        read_only_fields = ['username','password']
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password']) 
        return super().create(validated_data)