from django.urls import path
from . import views

urlpatterns = [
  path('add-user/', views.add_user, name='addUser'),
  path('update-user/<int:user_id>/', views.update_user, name='updateUser'),
  path('delete-user/<int:user_id>/', views.delete_user, name='deleteUser'),
  path('', views.index, name='users')
]