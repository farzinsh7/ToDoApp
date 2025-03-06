from rest_framework import permissions, viewsets
from .serializers import TodoSerializer
from .permissions import IsAuthor
from ...models import ToDo
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class TodoModelViewSet(viewsets.ModelViewSet):
    """ Getting Todo API For each Author by ModelViewSet """

    serializer_class = TodoSerializer
    permission_classes = [IsAuthor]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_date']
    
    def get_queryset(self):
        # Ensure only the authenticated user's todos are returned
        return ToDo.objects.filter(author=self.request.user)