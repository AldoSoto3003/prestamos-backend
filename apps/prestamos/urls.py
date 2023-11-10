from django.urls import path

from .views import ClientView,ClientListView

urlpatterns = [
    path('clients/',ClientListView.as_view(),name='clients'),
    path('client/<int:pk>/',ClientView.as_view(),name='client'),
    path('client/add/',ClientView.as_view(),name='client-add'),
    path('client/update/<int:pk>',ClientView.as_view(),name='client-update'),
    path('client/delete/<int:pk>',ClientView.as_view(),name='client-delete'),
]