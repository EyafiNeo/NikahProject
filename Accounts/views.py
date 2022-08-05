from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from Accounts.models import UserProfile,profileInfo, matching
from Accounts.serializers import UserProfileSerializer, profileInfoSerializer, matchingSerializer
from rest_framework import parsers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name',]

class profileInfoViewset(ModelViewSet):
    serializer_class = profileInfoSerializer
    queryset = profileInfo.objects.all()
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sex',]


class matchingViewset(ModelViewSet):
    serializer_class = matchingSerializer
    queryset = matching.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('who','toWhom')