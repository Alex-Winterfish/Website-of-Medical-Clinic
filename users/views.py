# -*- coding: utf-8 -*-
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
#from .forms import CustomUserCreationForm
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
from clinic import models

load_dotenv()

class RegisterView(generic.edit.CreateView):
    template_name = "users/register.html"
    #form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = os.getenv("EMAIL_HOST_USER")
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

    def form_invalid(self, form):
        print(form.errors)  # Вывод ошибок в консоль
        return render(self.request, self.template_name, {'form': form})

class UserPageView(generic.TemplateView):
    '''Контроллер для отображения страницы личного кабинета пользователя.'''
    template_name = 'users/user_page.html'

    def get_context_data(self, **kwargs):
        pass