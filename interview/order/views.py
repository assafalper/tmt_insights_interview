from django.db.models import F, Q
from django.utils.dateparse import parse_datetime

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request


from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


class OrderListbetweenEmbargoDates(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get(self, request: Request, *args, **kwargs) -> Response:
        date_str = request.GET.get("date")
        if not date_str:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=200)

        parsed_date = parse_datetime(date_str)
        if parsed_date is None:
            return Response("Invalid date format. Use ISO 8601.", status=400)

        filtered_qs = self.get_queryset().filter(
            Q(start_date__lte=parsed_date) & Q(embargo_date__gte=parsed_date)
        )

        serializer = self.serializer_class(filtered_qs, many=True)
        return Response(serializer.data, status=200)

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
