from django.shortcuts import render, redirect

from acoffe.models import coffe

from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

from acoffe.forms import RegistrationForm, LoginForm

# Реализовать домашнюю страницу, вывода списка предлагаемых кофе и страницы с подробным описанием

def home_page(request):
    return render(request, 'index.html')

# def list_coffe(request):
#     list_coffe = coffe.objects.all()
#     paginator = Paginator(list_coffe, 2)
#     page_num = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_num)

#     context = {
#         'list_coffe': list_coffe,
#         'page_obj': page_obj,
#         'title': 'Выбор кофе',
#     }
#     return render(request, 'acoffe/list_coffe.html', context)

def detail_coffe(reqest, coffe_id):
    detail_coffe = coffe.objects.get(pk=coffe_id)
    context = {
        'detail_coffe': detail_coffe,
    }
    return render(reqest, 'acoffe/detail_coffe.html', context)

class CoffeList(ListView):
    model = coffe
    template_name = 'acoffe/list_coffe.html'
    context_object_name = 'list_coffe'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выбор кофе'
        return context

def user_registration(request):
    if request.method == 'POST':
        # form = UserCreationForm(data=request.POST)
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('log in')
    else:
        # form = UserCreationForm()
        form = RegistrationForm()        
    return render(request, 'acoffe/auth/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        # form = AuthenticationForm(data=request.POST)
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = LoginForm()
    return render(request, 'acoffe/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_page')