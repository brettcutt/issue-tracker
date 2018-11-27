from django import forms
from .models import Bugs, Comments, Features


class BugsForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ['name', 'description']


class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ['name', 'description']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '4', 'cols': '5'}))

    class Meta:
        model = Comments
        fields = ['comment']
