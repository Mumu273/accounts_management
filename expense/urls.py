from django.urls import path
from .views import expense_category_list, expense_category_view

urlpatterns = [
    path('category_list', expense_category_list, name='expense_category_list'),
    path('category_view/<uuid:category_id>/', expense_category_view, name='expense_category_view'),]
