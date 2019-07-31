from rest_framework import serializers
from haraj_app.models import Add

class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add
        fields = '__all__'

