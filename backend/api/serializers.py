"""
Serializers for the API app
"""
from rest_framework import serializers


class LCMRequestSerializer(serializers.Serializer):
    """Serializer for LCM calculation request"""
    x = serializers.IntegerField(required=True, help_text="Starting number of the range")
    y = serializers.IntegerField(required=True, help_text="Ending number of the range")

    def validate(self, data):
        x = data.get('x')
        y = data.get('y')
        
        if x > y:
            raise serializers.ValidationError("x must be less than or equal to y")
        
        if x < 1 or y < 1:
            raise serializers.ValidationError("Both x and y must be positive integers")
        
        return data


class LCMResponseSerializer(serializers.Serializer):
    """Serializer for LCM calculation response"""
    x = serializers.IntegerField(help_text="Starting number of the range")
    y = serializers.IntegerField(help_text="Ending number of the range")
    result = serializers.IntegerField(help_text="The least common multiple")
