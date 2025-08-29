from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.views_api import JobApplicationViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r"jobs", JobApplicationViewSet, basename="jobs")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("applications.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/", include("api.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
