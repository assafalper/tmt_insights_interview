from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderListbetweenEmbargoDates


urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-detail"),
    path("", OrderListCreateView.as_view(), name="order-list"),
    path("embargo_date", OrderListbetweenEmbargoDates.as_view(), name="embargo_date-list"),
]
