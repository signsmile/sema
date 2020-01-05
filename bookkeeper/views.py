from django.shortcuts import render
from .models import Account, AccountEntry

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def account(request, account_id):
    account = Account.objects.get(accid=account_id)
    entry_list = AccountEntry.objects.filter(account=account_id)
    print(account)
    print(entry_list)
    context = {'entry_list': entry_list, 'balance': account.balance()}
    return render(request, 'bookkeeper/account.html', context)