"""
User admin view
"""
from django.contrib import admin
from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin view"""
    list_display = ('email', 'name', 'is_active', 'is_superuser')
    list_filter = ('is_active', 'is_superuser')
    search_fields = ('email', 'name')
    ordering = ('email',)
