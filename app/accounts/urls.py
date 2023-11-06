from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .views import (
    LoginView,
    RegistrationView,
    UserListView,
    AuthMeView
    )

urlpatterns = [
    path('login/',LoginView.as_view(),name='LoginView'),
    path('register_user/',RegistrationView.as_view(),name='RegisterView'),
    path('list_users/', UserListView.as_view(), name='list_users'),
    path('auth_me/', AuthMeView.as_view(), name='auth_me'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obatin_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]