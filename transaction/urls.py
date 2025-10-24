from django.urls import path
from .views import transaction_list

urlpatterns = [
    path('transaction_list', transaction_list, name='transaction_list'),
    # path('category_view/<uuid:category_id>/', category_view, name='category_view'),
    # path('add_new_category/<str:is_expense>/', add_new_category, name='add_new_category'),
    # path('category_edit/<uuid:category_id>/', category_edit, name='category_edit'),
    # path('category_delete/<uuid:category_id>/', category_delete, name='category_delete'),
]
