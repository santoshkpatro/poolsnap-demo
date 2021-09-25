import uuid
from django.db import models
from django.conf import settings
from items.models import Item


class Order(models.Model):
    ORDER_STATUS = (
        ('initiated', 'intitated'),
        ('processing', 'processing'),
        ('complete', 'complete'),
        ('discarded', 'discarded')
    )

    ORDER_TYPE = (
        ('default', 'default'),
        ('monthly_purchase', 'monthly_purchase'),
        ('monthly_renewal', 'monthly_renewal'),
        ('yearly_purchase', 'yearly_purchase'),
        ('yearly_renewal', 'yearly_renewal'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='orders')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='item_orders')

    type = models.CharField(max_length=20, default='default', choices=ORDER_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, default='initiated', choices=ORDER_STATUS)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'

    def __str__(self) -> str:
        return str(self.id)


class BillingDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'billing_details'

    def __str__(self) -> str:
        return str(self.id)
