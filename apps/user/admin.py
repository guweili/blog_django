from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _

User = get_user_model()


# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'nickname', 'icon', 'phone', 'email', 'sex', 'last_login', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('nickname', 'icon', 'email', 'phone', 'sex')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
