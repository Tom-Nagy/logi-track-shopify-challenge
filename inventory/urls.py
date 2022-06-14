''' home URL Configuration '''
from django.urls import path
from inventory import views


urlpatterns = [
    path('', views.index, name='home'),
    path('inventory_management', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('all_items/', views.all_items, name='all_items'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<item_id>/', views.edit_item, name='edit_item'),
    path('item_deletion/<item_id>/', views.item_deletion,
         name='item_deletion'),
]
