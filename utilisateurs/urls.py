# urls.py de votre application

from django.urls import path
from .views import LoginView, LogoutView, CreateUserView, UserListView, UserUpdateView, UserDeleteView, ActiveUsersListView, InactiveUsersListView, AdminUsersListView, UserDetailsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', CreateUserView.as_view(), name='create-user'),
    path('list/', UserListView.as_view(), name='list-users'),
    path('list/details/<int:pk>/', UserDetailsView.as_view(), name='details-user'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update-user'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
    path('list/actives/', ActiveUsersListView.as_view(), name='active-users'),
    path('list/inactives/', InactiveUsersListView.as_view(), name='inactive-users'),
    path('list/admins/', AdminUsersListView.as_view(), name='admin-users'),

    # Ajoutez d'autres URLs au besoin...
]
