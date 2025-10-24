from django.db import models
from abstract.base_model import BaseModel

class Category(BaseModel):
    category_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_expense = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name if self.category_name else ''

    class Meta:
        db_table = 'category'
        ordering = ['-created_at']
