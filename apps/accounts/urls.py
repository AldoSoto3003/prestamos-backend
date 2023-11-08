from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView


from .views import (
    LoginView,
    LogoutView,
    RegistrationView,
    UserListView,
    AuthMeView
    )

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('login/refresh/',TokenRefreshView.as_view(),name='login_refresh'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register_user/',RegistrationView.as_view(),name='register_user'),
    path('list_users/', UserListView.as_view(), name='list_users'),
    path('auth_me/', AuthMeView.as_view(), name='auth_me'),
]