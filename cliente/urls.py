from cliente.viewsets import ClienteViewSet

from rest_framework.routers import DefaultRouter

route = DefaultRouter()

route.register(r'nfe', ClienteViewSet, basename="Cliente")

urlpatterns = route.urls