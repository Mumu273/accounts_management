from django.urls import path
from .views import category_list, category_view, add_new_category, category_edit, category_delete

urlpatterns = [
    path('category_list', category_list, name='category_list'),
    path('category_view/<uuid:category_id>/', category_view, name='category_view'),
    path('add_new_category/<str:is_expense>/', add_new_category, name='add_new_category'),
    path('category_edit/<uuid:category_id>/', category_edit, name='category_edit'),
    path('category_delete/<uuid:category_id>/', category_delete, name='category_delete'),
]
