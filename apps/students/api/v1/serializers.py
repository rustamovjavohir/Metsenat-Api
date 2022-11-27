from rest_framework import serializers

from apps.students.models import StudentWallet


class StudentWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentWallet
        fields = ('id',
                  'student',
                  'degree', 'otm',
                  'contract_amount', 'donates',
                  'is_active', 'date_created')
