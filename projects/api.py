from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    # AllowAny cualquier cliente puede solicitar datos. Puede cambiarse por autenticated.
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer