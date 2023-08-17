from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from myapp.models import Student

channel_layer = get_channel_layer()

@receiver(post_save, sender=Student)
def send_fetch_signal(sender, instance, created, **kwargs):
    if not created:
        data = {
            'action': 'fetch'
        }
        async_to_sync(channel_layer.group_send)('websocket_group', {
            'type': 'update_items',
            'message': json.dumps(data)
        })
