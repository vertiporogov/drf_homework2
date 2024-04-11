from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework import generics

from materials.models import Payment
from materials.serializers.payment import PaymentListSerializer
from materials.services import get_link


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentListSerializer

    def perform_create(self, serializer):
        new_payment = serializer.save()
        product_name, payment_link, session_id = get_link(new_payment)
        new_payment.payment_link = payment_link
        new_payment.payment_id = session_id
        new_payment.save()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ('date_pay',)
