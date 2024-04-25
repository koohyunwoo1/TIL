from django import forms
from .models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['seller', 'buyer',]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', ]