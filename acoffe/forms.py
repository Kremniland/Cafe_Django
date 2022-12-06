from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from acoffe.models import coffe, ingridient

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя:',
        widget=forms.TextInput(attrs={'class': 'form-control', }),
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Ваш логин',
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    password = forms.CharField(
        label='Ваш пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )

class ContactForm(forms.Form):
    subject = forms.CharField(
        label='Заголовок',
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
        )
    )
    content = forms.CharField(
        label='Текст письма',
        widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 7,
        }
        )
    )

class CoffeAddForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        empty_value='Название',
        label='Название',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }
        )
    )
    price = forms.FloatField(
        label='Цена',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
                'aria-label':'With textarea',
            }
        )
    )
    ingridients = forms.ModelMultipleChoiceField(
        label='Ингридиенты',
        queryset=ingridient.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

class CoffeForm(forms.ModelForm):
    class Meta:
        model = coffe
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'descriptions': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),            
        }
