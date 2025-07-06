from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer

class ListingListCreate(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer