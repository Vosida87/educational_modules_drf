from rest_framework import serializers
from modules.models import EducationalModule


class EducationalModuleSerializer(serializers.ModelSerializer):
    order_number = serializers.IntegerField(source='id', read_only=True)  # порядковый номер берётся из id

    class Meta:
        model = EducationalModule
        fields = ['order_number', 'id', 'owner', 'title', 'description']
