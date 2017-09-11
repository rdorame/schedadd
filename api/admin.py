from django.contrib import admin
from .models import Son, Parent
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

#Define a Parent User
class ParentInline(admin.StackedInline):
    model = Parent
    can_delete = False
    verbose_name_plural = 'parents'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ParentInline, )

# Register your models here.

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Son)
