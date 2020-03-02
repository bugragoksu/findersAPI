from django.contrib import admin
from .models import Account
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
        list_display = ['email','city']
        list_display_links = ['email']
        search_fields = ['email','name','surname']


admin.site.register(Account,AccountAdmin)