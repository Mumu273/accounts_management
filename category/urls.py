from django.urls import path
from .views import category_list, category_view

urlpatterns = [
    path('category_list', category_list, name='category_list'),
    path('category_view/<uuid:category_id>/', category_view, name='category_view'),]
