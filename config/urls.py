from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clients.views import ClientViewSet, AccountViewSet, OrderViewSet, ProductViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('clients', ClientViewSet, 'clients')
router.register('accounts', AccountViewSet, 'accounts')
router.register('orders', OrderViewSet, 'orders')
router.register('products', ProductViewSet, 'products')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
