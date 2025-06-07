from django.contrib import admin
from .models import UserAuth


class UserAuthAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'username', 'dob')
    list_filter = ('first_name', 'username')
    search_fields = ('username', 'email')


admin.site.register(UserAuth, UserAuthAdmin)
