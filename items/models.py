import uuid
from django.db import models
from django.conf import settings
from category.models import Category


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='items')

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category_items')
    resource_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    yearly_price = models.DecimalField(max_digits=10, decimal_places=2)
    yearly_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    is_public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'items'

    def __str__(self) -> str:
        return str(self.id) + ' by ' + self.owner.name
