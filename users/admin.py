from django.contrib import admin

from users.models import CustomUser, FeedBackModel, ContentModel


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

@admin.register(ContentModel)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['company','about','email','email','email','email','address','map_address']
    list_filter = ['company',]
    search_help_text = 'company'