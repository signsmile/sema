from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Account, AccountEntry, Transaction


# Create your views here.
class IndexView(ListView):
    model = Account
    context_object_name = 'account_list'


class AccountView(DetailView):
    model = Account
    context_object_name = 'account'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['entries'] = self.object.entries.all()
    #     return context

class TransactionCreateView(CreateView):
    model = Transaction
    fields = ['t_stamp', 'description', 'project']


class AccountEntryCreateView(CreateView):
    model = AccountEntry
    fields = ['transaction', 'account', 'amount', 'description']