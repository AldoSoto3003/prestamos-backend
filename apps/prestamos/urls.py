from django.urls import path

from .views import (
    ClientView,
    ClientByNameView,
    ClientListView,
    LoanByNameView,
    LoanListView,
    MoneyLenderListByLoanView,
    MoneyLenderView,
    MoneyLenderListView,
    MoneyLenderByNameView,
    FundByMoneyLenderView,
    FundView,
    LoanView,
    PaymentView,
    )

urlpatterns = [
    path('client/get-all/',ClientListView.as_view(),name='client-get-all'),
    path('client/get/<int:pk>/',ClientView.as_view(),name='client-get-id'),
    path('client/get/<str:name>/',ClientByNameView.as_view(),name='client-get-name'),
    path('client/add/',ClientView.as_view(),name='client-add'),
    path('client/update/<int:pk>',ClientView.as_view(),name='client-update'),
    path('client/delete/<int:pk>',ClientView.as_view(),name='client-delete'),
    
    path('moneylender/get-all/',MoneyLenderListView.as_view(),name='moneylender-get-all'),
    path('moneylender/get/<int:pk>/',MoneyLenderView.as_view(),name='moneylender-get-id'),
    path('moneylender/get/<str:name>/',MoneyLenderByNameView.as_view(),name='client-get-name'),
    path('moneylender/add/',MoneyLenderView.as_view(),name='moneylender-add'),
    path('moneylender/update/<int:pk>',MoneyLenderView.as_view(),name='moneylender-update'),
    path('moneylender/delete/<int:pk>',MoneyLenderView.as_view(),name='moneylender-delete'),

    path('moneylender/loan/<int:pk>',MoneyLenderListByLoanView.as_view(),name='moneylender-get-by-loan'),

    path('fund/get-by-moneylender/<int:fk>',FundByMoneyLenderView.as_view(),name='fund-get-all'),
    path('fund/get/<int:pk>/',FundView.as_view(),name='fund-get-id'),
    path('fund/add/',FundView.as_view(),name='fund-add'),
    path('fund/update/<int:pk>',FundView.as_view(),name='fund-update'),
    path('fund/delete/<int:pk>',FundView.as_view(),name='fund-delete'),

    path('loan/add/',LoanView.as_view(),name='loan-add'),
    path('loan/get-all/',LoanListView.as_view(), name='loan-get-all'),
    path('loan/get/<str:name>/',LoanByNameView.as_view(), name='loan-by-name'),


    path('payment/add/',PaymentView.as_view(),name='payment-add'),
    # path('payment/get-all/'),

]