from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from .models import User
# Register your models here.


class UserAdmin(_UserAdmin):
    pass

admin.site.register(User, UserAdmin)
