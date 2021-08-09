from rest_framework.viewsets import ModelViewSet
from listing.models import Listing
from .serializer import ListingSerializer


class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer