import requests
import xmltodict
from rest_framework import generics
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response

from .get_signature import get_sig, get_salt
from .models import Transaction
from .serializers import TransactionSerializer

MERCHANT_ID = 535456
SECRET ="LeFnP16MP6AU6YKc"


class TransactionView(generics.ListCreateAPIView):
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
            pg_salt=get_salt(),
        )
        params['pg_sig'] = get_sig(params)
        r = requests.post('https://api.paybox.money/init_payment.php', params=params)
        print(r)
        payload = xmltodict.parse(r.content).get('response', {})
        if payload.get('pg_status') != 'ok':
            raise NotAcceptable
        return Response({"url": payload.get('pg_redirect_url')})


class TransactionStatusView(generics.ListAPIView):

    def ipn(request):
        from Paybox import Transaction

        # Your order object
        order = get_object_or_404(Order, reference=request.GET.get('RE'))

        transaction = Transaction()
        notification = transaction.verify_notification(response_url=request.get_full_path(), order_total=order.total)

        order.payment = notification['success']  # Boolean
        order.payment_status = notification['status']  # Paybox Status Message
        order.payment_auth_code = notification['auth_code']  # Authorization Code returned by Payment Center
        order.save()

        # Paybox Requires a blank 200 response
        return HttpResponse('')



