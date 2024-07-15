from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls"), name="users"),
    path("", include("system.urls"), name="system"),
    path("candidates/", include("candidates.urls"), name="candidates"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
