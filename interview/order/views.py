
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

class DeactivateOrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        order  = Order.objects.filter(id=kwargs["id"]).first()
        if order:
            order.is_active = False
            order.save(update_fields=['is_active'])
            return Response(self.serializer_class(order).data, status=200)

        else:
            return Response(f" order with {kwargs['id']} not found in system")


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
