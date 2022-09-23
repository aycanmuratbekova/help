from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from .get_signature import get_sig


MERCHANT_ID = 535456
SECRET ="LeFnP16MP6AU6YKc"


class Transaction(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        params = dict(
            pg_order_id=payment.id,
            pg_merchant_id=MERCHANT_ID,
            pg_amount=payment.amount,
            pg_description=payment.description,
            pg_salt=payment.salt,
        )
        params['pg_sig'] = get_sig(params)
        # print(params)
        r = requests.post('https://api.paybox.money/init_payment.php', params=params)
        return Response({"status": r.content})


