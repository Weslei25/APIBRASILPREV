from cliente.viewsets import ClienteViewSet, CadastrarClienteViewSet

from rest_framework.routers import DefaultRouter

route = DefaultRouter()

route.register(r'show_clientes', ClienteViewSet, basename="Cliente")
route.register(r'cadastrar', CadastrarClienteViewSet, basename="cadastrar_cliente")

urlpatterns = route.urls