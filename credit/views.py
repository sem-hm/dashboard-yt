from typing import Any, Dict
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from credit.models import Bank

# Create your views here.
def bank_list_view(request):
    list_bank_obj = Bank.objects.all()
    paginator = Paginator(list_bank_obj, 10)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context = {}
    context['list_bank_obj'] = page_obj.object_list
    context['page_obj'] = page_obj
    return render(request,'credit/bank_list.html', context)

class BankListView(ListView):
    model = Bank
    context_object_name = 'list_bank_obj'
    paginate_by = 5

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['hola'] = 'Saludos buen dia'
        return context