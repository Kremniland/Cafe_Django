from django.shortcuts import render

from acoffe.models import coffe

from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator

# Реализовать домашнюю страницу, вывода списка предлагаемых кофе и страницы с подробным описанием

def home_page(request):
    return render(request, 'index.html')

def list_coffe(request):
    list_coffe = coffe.objects.all()
    paginator = Paginator(list_coffe, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        'list_coffe': list_coffe,
        'page_obj': page_obj,
        'title': 'Выбор кофе',
    }
    return render(request, 'acoffe/list_coffe.html', context)

def detail_coffe(reqest, coffe_id):
    detail_coffe = coffe.objects.get(pk=coffe_id)
    context = {
        'detail_coffe': detail_coffe,
    }
    return render(reqest, 'acoffe/detail_coffe.html', context)

# class CoffeList(ListView):
#     model = coffe
#     template_name = 'acoffe/list_coffe.html'
#     context_object_name = 'list_coffe'
#     paginate_by = 2

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Выбор кофе'
#         return context
