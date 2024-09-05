from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Listing
from .serializers import ListingSerializer
from django.db.models import Q

@api_view(['GET', 'POST'])
def listing_list_create(request):
    if request.method == 'GET':
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def listing_detail(request, pk):
    try:
        listing = Listing.objects.get(pk=pk)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListingSerializer(listing)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def search_listings(request):
    query = request.query_params.get('q', '')
    listings = Listing.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(category__icontains=query)
    )
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filter_listings(request):
    category = request.query_params.get('category', None)
    min_price = request.query_params.get('min_price', None)
    max_price = request.query_params.get('max_price', None)

    listings = Listing.objects.all()

    if category:
        listings = listings.filter(category=category)
    if min_price:
        listings = listings.filter(price__gte=min_price)
    if max_price:
        listings = listings.filter(price__lte=max_price)

    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)
