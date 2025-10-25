from django.urls import path
from .views import transaction_list, add_new_transaction, transaction_view, transaction_edit, transaction_delete

urlpatterns = [
    path('transaction_list', transaction_list, name='transaction_list'),
    path('transaction_view/<uuid:transaction_id>/', transaction_view, name='transaction_view'),
    path('add_new_transaction/<str:is_expense>/', add_new_transaction, name='add_new_transaction'),
    path('transaction_edit/<uuid:transaction_id>/', transaction_edit, name='transaction_edit'),
    path('transaction_delete/<uuid:transaction_id>/', transaction_delete, name='transaction_delete'),
]
