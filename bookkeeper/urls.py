from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/<int:account_id>/', views.account, name='Account'),
]