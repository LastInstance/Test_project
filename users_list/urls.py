from django.urls import path, include
from . import views

app_name = 'users_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('users/add-user', views.add_user, name='add_user'),
    path('users/edit/<int:user_id>', views.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', views.del_user, name='del_user'),
    path('groups/', views.groups, name='groups'),
    path('groups/add-group', views.add_group, name='add_group'),
    path('groups/edit/<int:group_id>/', views.edit_group, name='edit_group'),
    path('groups/delete/<int:group_id>/', views.delete_group, name='delete_group'),

]