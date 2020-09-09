from rest_framework.serializers import ModelSerializer

from .models import Laptop


class LaptopSerializer(ModelSerializer):
    class Meta:
        model = Laptop
        fields = ('name', 'cpu', 'company',)
