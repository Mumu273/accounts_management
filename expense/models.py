from django.db import models
from abstract.base_model import BaseModel

class ExpenseCategory(BaseModel):
    category_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'expense_category'
