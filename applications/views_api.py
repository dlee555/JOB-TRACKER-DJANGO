from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import JobApplication
from .serializers import JobApplicationSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["company", "job_title"]
    ordering_fields = ["date_applied", "company", "status"]
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # each user sees only their own data (REST principle: resource scoping)
        return JobApplication.objects.filter(user=self.request.user).order_by("-date_applied")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
