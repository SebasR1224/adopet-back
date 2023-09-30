from rest_framework import viewsets
from .serializer import AnimalsSerializer
from .models import Animals

# Create your views here.
class AnimalsView(viewsets.ModelViewSet):
    serializer_class = AnimalsSerializer
    queryset = Animals.objects.all()
