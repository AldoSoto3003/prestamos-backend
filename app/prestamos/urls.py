from django.urls import path

from .views import PruebaAPI

urlpatterns = [
    path('prueba/',PruebaAPI.as_view(),name='prueba'),
]