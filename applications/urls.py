from django.urls import path
from .views import (
    ApplicationListView, ApplicationCreateView,
    ApplicationUpdateView, ApplicationDeleteView,
)

# app_name creates a namespace "applications:" for URL names
app_name = "applications"

urlpatterns = [
    path("", ApplicationListView.as_view(), name="list"),          # GET /
    path("new/", ApplicationCreateView.as_view(), name="create"),  # GET/POST /new/
    path("<int:pk>/edit/", ApplicationUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ApplicationDeleteView.as_view(), name="delete"),
]