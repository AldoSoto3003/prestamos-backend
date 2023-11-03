from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from app.accounts.views import LoginView,RegistrationView

# urlpatterns = [
#     path('login/',login_view, name='login'),    
#     path('register/',registration_view, name='register'),
#     path('logout/',logout_view, name='logout'),
    
#     path('api/token/',TokenObtainPairView.as_view(),name='token_obatin_pair'),
#     path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
# ]

urlpatterns = [
    path('login/',LoginView.as_view(),name='LoginView'),
    path('register_user/',RegistrationView.as_view(),name='RegisterView')
]