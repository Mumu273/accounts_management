from django.forms import ModelForm
from .models import Transaction
from external.exclude_list import exclude_list
from category.models import Category

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = exclude_list


    def __init__(self, *args, **kwargs):
        is_expense = kwargs.pop('is_expense', None)
        super().__init__(*args, **kwargs)
        if is_expense is not None:
            self.fields['category'].queryset = Category.objects.filter(is_expense=is_expense)

