from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from system.apps import SystemConfig
from system.views import ContactsView, base

app_name = SystemConfig.name


urlpatterns = [
    path("", base, name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
