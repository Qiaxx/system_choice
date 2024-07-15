from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "date_born", "address")
    list_filter = ("email",)
    search_fields = ("id", "email", "date_born", "address")
