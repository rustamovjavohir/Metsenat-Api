from django.contrib import admin

from apps.students.models import StudentWallet


class SA(admin.ModelAdmin):
    list_display = ('id', 'student', 'degree', 'otm', 'donates', 'contract_amount', 'is_active')
    list_display_links = ('id', 'student')
    search_fields = ['Student']
    search_help_text = 'Search student'
    list_filter = ('degree', 'otm')


admin.site.register(StudentWallet, SA)
