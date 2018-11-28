from django import forms
from .models import Features


class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ['name', 'description']
