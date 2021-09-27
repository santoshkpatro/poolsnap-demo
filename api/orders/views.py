import uuid
import shortuuid
from django.http.response import Http404
from django.utils import timezone
from datetime import timedelta
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from items.models import Item
from orders.models import Order
from licenses.models import License
from .serializers import OrderSerializer
from .permissions import IsOwner


class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        orders = super().get_queryset()
        return orders.filter(user=self.request.user).order_by('created_at')


class OrderDetail(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def order_create(request, item_id):
    order_type = request.query_params['type']
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404

    if order_type == 'monthly_purchase':
        order = Order(user=request.user, item=item, type=order_type,
                      price=item.monthly_price, amount=item.monthly_price)
    elif order_type == 'yearly_purchase':
        order = Order(user=request.user, item=item, type=order_type, price=item.yearly_price, amount=item.yearly_price)

    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated, IsOwner))
def order_process(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        raise Http404

    payment_status = request.query_params['status']

    if payment_status == 'success':
        order.payment_id = shortuuid.uuid()
        order.transaction_id = uuid.uuid4()

        if order.type == 'yearly_purchase':
            validity = timezone.now() + timedelta(days=30)
        else:
            validity = timezone.now() + timedelta(days=365)

        License.objects.create(user=request.user, item=order.item, valid_upto=validity)

        order.status = 'complete'
        order.save()
    else:
        order.status = 'processing'
        order.save()

    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
