from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'patronymic', 'email']
    list_filter = ['last_name', 'first_name', 'patronymic', 'email']
    search_help_text = 'last_name'
