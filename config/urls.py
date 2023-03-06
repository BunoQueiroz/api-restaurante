from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clients.views import ClientViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('clients', ClientViewSet, 'clients')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
