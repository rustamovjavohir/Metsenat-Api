from django.contrib import admin
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth

from apps.accounts.models import Account
from apps.donate.models import Donate
from apps.sponsors.models import SponsorWallet


class SponsorWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'sponsor', 'sponsor_wallet', 'spent_amounts', 'date_created', 'status', 'is_active')
    list_filter = ('status', 'sponsor_wallet', 'date_created')
    search_fields = ['sponsor']
    search_help_text = 'Search Sponsor'


admin.site.register(SponsorWallet, SponsorWalletAdmin),


