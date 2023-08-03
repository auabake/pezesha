
from django.urls import path
from .views import AccountCreateView, AccountDetailView, MoneyTransferView, AccountListView

urlpatterns = [
    path('accounts/', AccountCreateView.as_view(), name='account_create'),
    path('accounts/list/', AccountListView.as_view(), name='account_list'),
    path('accounts/<int:id>/', AccountDetailView.as_view(), name='account_detail'),
    path('accounts/transfer/', MoneyTransferView.as_view(), name='send'),
]
