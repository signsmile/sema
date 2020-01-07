from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('account/<int:pk>/', views.AccountView.as_view(), name='account'),
    path('transaction/add',
         views.TransactionCreateView.as_view(),
         name='add_transaction'),
    path('accountentry/add',
         views.AccountEntryCreateView.as_view(),
         name='add_accountentry'),
]