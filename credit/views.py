from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from credit.models import Bank

# Create your views here.
def bank_list_view(request):
    list_bank_obj = Bank.objects.all()
    context = {}
    context['list_bank_obj'] = list_bank_obj
    return render(request,'credit/bank_list.html', context)

class BankListView(ListView):
    model = Bank
    context_object_name = 'list_bank_obj'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['hola'] = 'Saludos buen dia'
        return context