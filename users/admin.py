from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

UserAdmin.add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','roll_no','dob','email', 'password1', 'password2')}
        ),
    )


class AccountAdmin(UserAdmin):
    list_display = (
        'username','roll_no','dob','email','is_student','is_teacher'
    )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)
