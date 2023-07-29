from rest_framework import serializers
from .models import Xnara

class XnaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xnara
        fields = "__all__"