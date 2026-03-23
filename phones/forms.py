from django import forms
from .models import MobilePhone, Brand

class MobilePhoneForm(forms.ModelForm):
    class Meta:
        model = MobilePhone
        fields = ['brand', 'model_name', 'price', 'storage', 'ram', 'battery', 'condition', 'in_stock']
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. iPhone 15 Pro'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 999.99'}),
            'storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 256GB'}),
            'ram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 12GB'}),
            'battery': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 4500mAh'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Samsung'}),
        }
