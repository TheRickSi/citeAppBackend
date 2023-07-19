from rest_framework import serializers
from .models import *
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields = '__all__'
        read_only_fields = ['username','password']
        
    def update(self, instance, validated_data):
        print(instance.favcite.id)
        return super().update(instance, validated_data)