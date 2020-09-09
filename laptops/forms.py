from django.forms import ModelForm
from .models import Laptop


class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        fields = ('name', 'ram')