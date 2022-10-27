from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("slackUsername", "backend","Age")
    search_fields = ("slackUsername", "backend","Age")
admin.site.register(User, UserAdmin)