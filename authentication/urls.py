from django.urls import path
from .views import *
urlpatterns = [
    path('', login_view, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout_view, name='logout'),
]
