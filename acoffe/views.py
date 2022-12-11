from django.shortcuts import render, redirect, get_object_or_404

from acoffe.models import coffe, ingridient

from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from django.urls import reverse_lazy

from django.contrib.auth import login, logout

from acoffe.forms import RegistrationForm, LoginForm, ContactForm, CoffeForm, CoffeAddForm

from django.core.mail import send_mail
from django.conf import settings

# MESSAGES
from django.contrib import messages

# API
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from acoffe.serializers import CoffeSerializer, IngridientSerializer

# REGISTER PERMISSION
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

# BASKET
from basket.forms import BasketAddProductForm


def home_page(request):
    return render(request, 'index.html', {'title': 'Домашняя страница'})

def detail_coffe(reqest, coffe_id):
    detail_coffe = coffe.objects.get(pk=coffe_id)
    context = {
        'detail_coffe': detail_coffe,
# Добавляем корзину:
        'basket_form': BasketAddProductForm(),
    }
    return render(reqest, 'acoffe/detail_coffe.html', context)

def get_add_coffe(request):
    if request.method == 'POST':
        coffe_form = CoffeAddForm(request.POST)
        if coffe_form.is_valid():
            coffe_add = coffe.objects.create(
                name=coffe_form.cleaned_data['name'],
                description=coffe_form.cleaned_data['description'],
                price=coffe_form.cleaned_data['price'],
                )
            for ingridient in coffe_form.cleaned_data['ingridients']:
                coffe_add.ingridients.add(ingridient)
            return redirect('list_coffe')           
    else:
        coffe_form = CoffeAddForm()
    context = {
        'form': coffe_form,
    }
    return render(request, 'acoffe/create_coffe.html', context)

class CoffeList(ListView):
    model = coffe
    template_name = 'acoffe/list_coffe.html'
    context_object_name = 'list_coffe'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выбор кофе'
        return context

class CoffeDelete(DeleteView):
    model = coffe
    template_name = 'acoffe/delete_coffe.html'
    pk_url_kwarg = 'coffe_id'
    success_url = reverse_lazy('list_coffe')

    @method_decorator(permission_required('coffe.delete_coffe'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CoffeUpdate(UpdateView):
    model = coffe
    form_class = CoffeForm
    template_name = 'acoffe/update_coffe.html'
    pk_url_kwarg = 'coffe_id'
    success_url = reverse_lazy('list_coffe')

    @method_decorator(permission_required('coffe.change_coffe'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class CoffeCreate(CreateView):
    model = coffe
    form_class = CoffeForm
    template_name = 'acoffe/create_coffe.html'
    success_url = reverse_lazy('list_coffe')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('log in')
    else:
        form = RegistrationForm()        
    return render(request, 'acoffe/auth/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
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

# EMAIL

def contact_email(request): 
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            print(form.cleaned_data)
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                settings.EMAIL_HOST_USER,
                ['kremnilandk@gmail.com'],
                fail_silently=False
                )
            if mail: 
                messages.success(request, 'Письмо успешно отправлено.') 
                return redirect('list_coffe') 
            else: 
                messages.error(request, 'Письмо не удалось отправить, попробуйте позже.') 
        else: 
            messages.warning(request, 'Письмо неверно заполнено, перепроверьте внесенные данные.') 
    else: 
        form = ContactForm() 
    return render(request, 'acoffe/email.html', {'form': form, 'title': 'Отзывы'})

# API
@api_view(['GET', 'POST']) # Добавит csrf_token при обращении к апи
def coffe_api_list(request):
    if request.method == 'GET':
        coffe_list = coffe.objects.all()
        serializer = CoffeSerializer(coffe_list, many=True)
        return Response({'coffe': serializer.data})
    elif request.method == 'POST':
        serializer = CoffeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def coffe_api_detail(request, pk):
    coffe_obj = get_object_or_404(coffe, pk=pk)
    if request.method == 'GET':
        serializer = CoffeSerializer(coffe_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CoffeSerializer(coffe_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Данные успешно обновлены', 'coffe': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        coffe_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)

class CoffeViewSet(viewsets.ModelViewSet):
    queryset = coffe.objects.all()
    serializer_class = CoffeSerializer

class IngridientViewSet(viewsets.ModelViewSet):
    queryset = ingridient.objects.all()
    serializer_class = IngridientSerializer

# ERROR

def error_404(request, exception):
    response = render(request, 'acoffe/error/error.html', {'title': 'Страница не найдена', 'message': exception})
    # При переопределении вернет статусный код
    response.status_code = 404
    return response
