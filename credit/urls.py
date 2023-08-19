from django.urls import path
from .views import bank_list_view, BankListView

urlpatterns = [
    path('', bank_list_view, name='credit-index'),
    path('cbv/', BankListView.as_view(), name='credit-listview-bank'),
]