from rest_framework import serializers
from .models import VisaRequests

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaRequests
        fields = '__all__'