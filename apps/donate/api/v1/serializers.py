from rest_framework import serializers

from apps.donate.models import Donate


class DonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donate
        fields = ('id', 'sponsor', 'student', 'donate', 'date_created')

    def validate(self, attrs):
        print(attrs)
        sponsor__wallet = attrs.get('sponsor').sponsor_wallet
        contract_amount = attrs.get('student').contract_amount
        donate = attrs.get('donate')
        if donate > sponsor__wallet:
            raise serializers.ValidationError({'sponsor__wallet': 'Yetarli emas'})
        elif donate > contract_amount:
            raise serializers.ValidationError({'contract_amount': 'Siz kiritgan summa keragidan ortiq'})
        return attrs
