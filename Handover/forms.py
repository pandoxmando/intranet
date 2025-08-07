from django import forms
from . import models

class CreateHandover(forms.ModelForm):
    class Meta:
        model = models.Handover
        fields = ['ho_date', 'asset', 'staff', 'approved_by_hr', 'approved_by_it', 'approved_by_comment']


class CreateHandoverReturn(forms.ModelForm):
    class Meta:
        model = models.HandoverReturn
        fields = ['hr_date', 'asset', 'staff', 'return_date', 'return_condition']

