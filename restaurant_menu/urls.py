from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuList.as_view(), name='menu'),  # the class in views.py
    path('menuitem/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item'),
    path('about/', views.AboutView.as_view(), name='about')
]