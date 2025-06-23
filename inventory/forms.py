from django import forms
from .models import Item, Stock

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name',
                'required': 'required'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Item.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("An item with this name already exists.")
        return name


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            'item',
            'quantity',
            'price',
            'wholeseller_price',
            'retailer_price',
            'description'
        ]
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter stock quantity',
                'required': 'required'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
                'step': '0.01'
            }),
            'wholeseller_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter wholeseller price',
                'step': '0.01'
            }),
            'retailer_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter retailer price',
                'step': '0.01'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description',
                'rows': 3
            }),
        }
