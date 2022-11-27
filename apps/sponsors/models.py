from django.db import models
from django.db.models import Sum

from apps.accounts.models import Account
from apps.donate.models import Donate
from apps.university.models import STATUS


class SponsorWallet(models.Model):
    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"

    sponsor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,
                                limit_choices_to={'is_sponsor': True, 'is_active': True})
    sponsor_wallet = models.FloatField(default=0.0)
    spent_amount = models.FloatField(default=0.0)
    status = models.IntegerField(choices=STATUS, default=0)
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.sponsor.phone

    def spent_amounts(self):
        spent_amount = Donate.objects.filter(sponsor_id=self.id).aggregate(
            Sum('donate'))
        if spent_amount.get('donate__sum'):
            spent_amount = self.sponsor_wallet - spent_amount.get('donate__sum')
        else:
            return 0
        print(spent_amount)
        return spent_amount

    def wallet_avg(self):
        spent_amount = Donate.objects.filter(sponsor_id=self.id).aggregate(Sum('donate'))
        return spent_amount.get('donate__sum')
