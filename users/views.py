# -*- coding: utf-8 -*-
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from users import forms
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
from users import models, forms

load_dotenv()

class RegisterView(generic.edit.CreateView):
    template_name = "users/register.html"
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("clinic:main")


    def form_invalid(self, form):
        print(form.errors)  # Вывод ошибок в консоль
        return render(self.request, self.template_name, {'form': form})

class UserPageView(generic.TemplateView):
    '''Контроллер для отображения страницы личного кабинета пользователя.'''
    template_name = 'users/user_page.html'

    def get_context_data(self, **kwargs):
        pass

class FeedBackCreateView(generic.CreateView):
    '''Контроллер для создания экземпляра model:users.models.FeedBackmodel.'''
    template_name = 'users/feedback_form.html'
    model = models.FeedBackModel
    form_class = forms.FeedBackForm
    success_url = reverse_lazy('clinic:main')