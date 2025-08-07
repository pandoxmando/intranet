from django import forms
from . import models

class CreateAsset(forms.ModelForm):
    class Meta:
        model = models.Asset
        fields = ['code', 'serial_number', 'specs', 'category']

