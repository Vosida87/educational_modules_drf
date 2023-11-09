from rest_framework import serializers
from modules.models import EducationalModule


class EducationalModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalModule
        fields = ['id', 'owner', 'title', 'description']