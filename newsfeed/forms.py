from django import forms
from .models import Product

class PostProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'image', 'mobile_number', 'location')