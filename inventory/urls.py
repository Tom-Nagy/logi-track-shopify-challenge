''' home URL Configuration '''
from django.urls import path
from inventory import views


urlpatterns = [
    path('', views.index, name='home'),
    path('inventory_management', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('all_items/', views.all_items, name='all_items'),
]
