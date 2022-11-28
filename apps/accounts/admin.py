from django.contrib import admin

from apps.accounts.models import Account



class AccountAdmin(admin.ModelAdmin):
    search_fields = ['username']
    search_help_text = 'search username'
    list_filter = ['is_staff', 'is_sponsor', 'is_student']
    list_display = (
        'id', 'username', 'phone', 'gender', 'image_tag', 'date_login', 'date_created', 'is_active',)
    readonly_fields = ('date_login', 'date_created')
    list_display_links = ('id', 'username',)


admin.site.register(Account, AccountAdmin)
