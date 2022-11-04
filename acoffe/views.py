from django.shortcuts import render

from acoffe.models import coffe

# Реализовать домашнюю страницу, вывода списка предлагаемых кофе и страницы с подробным описанием

def home_page(request):
    return render(request, 'index.html')

def list_coffe(request):
    list_coffe = coffe.objects.all()
    context = {
        'list_coffe': list_coffe,
    }
    return render(request, 'acoffe/list_coffe.html', context)

def detail_coffe(reqest, coffe_id):
    detail_coffe = coffe.objects.get(pk=coffe_id)
    context = {
        'detail_coffe': detail_coffe,
    }
    return render(reqest, 'acoffe/detail_coffe.html', context)
