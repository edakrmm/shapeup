from django.contrib import admin
from shapeup.models import CustomUserModel

from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (('Avatar Değiştirme Alanı', {'fields': ['avatar']}),)