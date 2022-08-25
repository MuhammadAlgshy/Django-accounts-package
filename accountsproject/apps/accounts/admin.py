from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

if settings.USER_NOPASSWORD:
    class UserCreationForm(UserCreationForm):
        """
        A UserCreationForm with optional password inputs.
        """

        def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.fields['password1'].required = False
            self.fields['password2'].required = False
            # If one field gets autocompleted but not the other, our 'neither
            # password or both password' validation will be triggered.
            self.fields['password1'].widget.attrs['autocomplete'] = 'off'
            self.fields['password2'].widget.attrs['autocomplete'] = 'off'

        def clean_password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = super(UserCreationForm, self).clean_password2()
            if bool(password1) ^ bool(password2):
                raise forms.ValidationError("Fill out both fields")
            return password2

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    if settings.USER_NOPASSWORD:
        add_form= UserCreationForm
        add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email","is_active")}),
    )
    else:
        add_fieldsets = (
            (None, {"classes": ("wide",), "fields": ("email","password1","password2",)}),
        )
    readonly_fields = ("last_login", "updatedDate", "createdDate","deletedDate")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "updatedDate",
                    "createdDate",
                )
            },
        ),
    )
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
       "createdDate",
        "updatedDate",
    )
    search_fields = ("id", "email")
    ordering = ("createdDate",)
    date_hierarchy = "updatedDate"
    filter_horizontal = ("groups", "user_permissions")
    actions=['activate_user', 'deactivate_user']
    exclude = ('password',)
    
    def has_delete_permission(self, request, obj=None) :
        return settings.USER_USER_DELETE
        
  
    @admin.action(description='Activate User')
    def activate_user(self, request, queryset):
        user = queryset.update(is_active=True)
        self.message_user(
            request,
            f'{user} User has been activated!'
        )

    @admin.action(description='Deactivate User')
    def deactivate_user(self, request, queryset):
        user = queryset.update(is_active=False)
        self.message_user(
            request,
            f'{user} User has been deactivated!'
        )
