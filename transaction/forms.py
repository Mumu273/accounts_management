from django.forms import ModelForm
from .models import Transaction
from external.exclude_list import exclude_list

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = exclude_list

