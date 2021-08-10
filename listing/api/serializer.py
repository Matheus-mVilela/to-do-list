from rest_framework.serializers import ModelSerializer
from listing.models import Listing


class ListingSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields = ('__all__')