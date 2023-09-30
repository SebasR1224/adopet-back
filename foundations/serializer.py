from rest_framework import serializers
from .models import Foundation

class FoundationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foundation
        fields = '__all__'