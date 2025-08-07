from django import forms
from . import models

class CreateAsset(forms.ModelForm):
    class Meta:
        model = models.Asset
        fields = ['reg_number', 'name', 'department']

