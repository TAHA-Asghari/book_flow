from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    fieldsets = ((None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2')}),
                 (None, {'fields': ('age',)}))

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2')}),
        (None, {'fields': ('age',)}))

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        print("DEBUG: Fieldsets ->", fieldsets)  # This will print the fieldsets in the terminal
        return fieldsets


admin.site.register(CustomUser, CustomUserAdmin)











