from django.contrib import admin

from apps.donate.models import Donate


class DonateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sponsor', 'student', 'donate', 'date_created')


admin.site.register(Donate, DonateAdmin)
