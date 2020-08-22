from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetSearchForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['IP_address', 'hostname', 'user_email']
