from django.urls import path
from .views import category_list, category_view, add_new_category

urlpatterns = [
    path('category_list', category_list, name='category_list'),
    path('category_view/<uuid:category_id>/', category_view, name='category_view'),
    path('add_new_category/<str:is_expense>/', add_new_category, name='add_new_category'),

]
