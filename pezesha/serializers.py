
from rest_framework import serializers
from .models import Accounts

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Accounts
        fields = ('id', 'account_name', 'account_type','balance')


class MoneyTransferSerializer(serializers.Serializer):
    from_account = serializers.IntegerField()
    to_account = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
