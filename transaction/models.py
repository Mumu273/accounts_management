from django.db import models
from abstract.base_model import BaseModel
from category.models import Category

class Transaction(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    transaction_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField()
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_name} {self.category.category_name}"

    class Meta:
        db_table = 'transaction'
        ordering = ['-created_at']
