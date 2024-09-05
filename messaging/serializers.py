from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')
    listing = serializers.ReadOnlyField(source='listing.title')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'listing', 'content', 'timestamp']
