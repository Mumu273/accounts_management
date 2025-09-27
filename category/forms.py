from django import forms
from .models import Category
from external.exclude_list import exclude_list

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = exclude_list
