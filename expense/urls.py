from django.urls import path
from .views import expense_category_list

urlpatterns = [
    path('category_list', expense_category_list, name='expense_category_list'),
    ]
