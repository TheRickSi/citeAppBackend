from rest_framework import serializers
from .models import *

class CiteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Cite
        fields = "__all__"