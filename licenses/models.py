import uuid
from django.db import models
from django.conf import settings
from items.models import Item


class License(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='licenses')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    valid_upto = models.DateField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'licenses'

    def __str__(self) -> str:
        return str(self.id)
