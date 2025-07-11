from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Customizes the display of UserProfile in the Django admin interface.
    """
    list_display = ('name', 'email', 'github', 'leetcode', 'codeforces', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

