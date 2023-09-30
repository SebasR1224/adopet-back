from rest_framework import viewsets
from .serializer import FoundationSerializer
from .models import Foundation

# Create your views here.
class FoundationView(viewsets.ModelViewSet):
    serializer_class = FoundationSerializer
    queryset = Foundation.objects.all()
