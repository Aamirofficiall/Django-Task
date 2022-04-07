from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from accounts.models import CustomUser,Role
from django.contrib import admin

User=get_user_model()



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser','role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser','role')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)
