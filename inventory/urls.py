from django.urls import path
from . import views


urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add/', views.add_item, name='add_item'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update_item'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete_item'),
]
