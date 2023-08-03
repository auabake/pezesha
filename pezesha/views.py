from decimal import Decimal

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Accounts
from .serializers import AccountSerializer, MoneyTransferSerializer


class AccountListView(generics.ListAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountCreateView(generics.CreateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountDetailView(generics.RetrieveAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "id"
    permission_classes = [permissions.IsAuthenticated]


class MoneyTransferView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = MoneyTransferSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        from_account_id = request.data.get("from_account")
        to_account_id = request.data.get("to_account")
        amount = Decimal(str(request.data.get("amount")))

        if amount <= 0:
            return Response(
                {"message": "Amount must be a positive value"}, status=status.HTTP_400_BAD_REQUEST
        )

        try:
            from_account = Accounts.objects.get(id=from_account_id)
            to_account = Accounts.objects.get(id=to_account_id)
        except Accounts.DoesNotExist:
            return Response(
                {"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if from_account.balance < amount:
            return Response(
                {"message": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST
            )

        from_account.balance -= amount
        to_account.balance += amount

        from_account.save()
        to_account.save()

        return Response({"message": "Transfer successful"}, status=status.HTTP_200_OK)
