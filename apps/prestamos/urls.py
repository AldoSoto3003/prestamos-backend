from django.urls import path

from .views import ClientView,ClientListView,MoneyLenderView,MoneyLenderListView

urlpatterns = [
    path('client/get-all/',ClientListView.as_view(),name='client-get-all'),
    path('client/get/<int:pk>/',ClientView.as_view(),name='client-get-id'),
    path('client/add/',ClientView.as_view(),name='client-add'),
    path('client/update/<int:pk>',ClientView.as_view(),name='client-update'),
    path('client/delete/<int:pk>',ClientView.as_view(),name='client-delete'),
    
    
    path('moneylender/get-all/',MoneyLenderListView.as_view(),name='moneylender-get-all'),
    path('moneylender/get/<int:pk>/',MoneyLenderView.as_view(),name='moneylender-get-id'),
    path('moneylender/add/',MoneyLenderView.as_view(),name='moneylender-add'),
    path('moneylender/update/<int:pk>',MoneyLenderView.as_view(),name='moneylender-update'),
    path('moneylender/delete/<int:pk>',MoneyLenderView.as_view(),name='moneylender-delete'),
]