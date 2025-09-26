from django import forms
from .models import ExpenseCategory
from external.exclude_list import exclude_list

class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        exclude = exclude_list
