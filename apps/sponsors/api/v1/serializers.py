from rest_framework import serializers

from apps.sponsors.models import SponsorWallet


class SponsorWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorWallet
        fields = (
            'id',
            'sponsor',
            'sponsor_wallet',
            'spent_amounts',
            'status',
            'spent_amount',
            'wallet_avg',
            'is_active',
            'date_created'
        )


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorWallet
        fields = ('sponsor', 'sponsor_wallet')

