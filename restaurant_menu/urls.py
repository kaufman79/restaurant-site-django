from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),  # the class in views.py
    path('menuitem/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item')
]