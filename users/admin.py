from django.contrib import admin

from users.models import CustomUser, FeedBackModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "patronymic", "email"]
    list_filter = ["last_name", "first_name", "patronymic", "email"]
    search_help_text = "last_name"


@admin.register(FeedBackModel)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ["theme", "email", "feed_back"]
    list_filter = ["theme", "email", "feed_back"]
    search_help_text = "theme"
