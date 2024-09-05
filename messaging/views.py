from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from listings.models import Listing
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def send_message(request):
    sender = request.user
    receiver_username = request.data.get('receiver')
    listing_id = request.data.get('listing')
    content = request.data.get('content')

    if not receiver_username or not listing_id or not content:
        return Response({"detail": "Receiver, listing, and content are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        receiver = User.objects.get(username=receiver_username)
    except User.DoesNotExist:
        return Response({"detail": "Receiver not found."}, status=status.HTTP_404_NOT_FOUND)

    try:
        listing = Listing.objects.get(id=listing_id)
    except Listing.DoesNotExist:
        return Response({"detail": "Listing not found."}, status=status.HTTP_404_NOT_FOUND)

    message = Message.objects.create(sender=sender, receiver=receiver, listing=listing, content=content)
    serializer = MessageSerializer(message)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def inbox(request):
    user = request.user
    messages = Message.objects.filter(receiver=user).order_by('-timestamp')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def sent_messages(request):
    user = request.user
    messages = Message.objects.filter(sender=user).order_by('-timestamp')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
