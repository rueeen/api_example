from .models import Note
from .serializers import NoteSerializer
from rest_framework import viewsets

# Create your views here.
class NoteApiView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
