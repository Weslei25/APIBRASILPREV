from plano.viewsets import PlanoViewSet, AporteExtraViewSet, ResgateViewSet

from rest_framework.routers import DefaultRouter

route = DefaultRouter()

route.register(r'contratar_plano', PlanoViewSet, basename="contratar_plano")
route.register(r'aporte_extra', AporteExtraViewSet, basename="aporte_extra")
route.register(r'resgate', ResgateViewSet, basename="aporte_extra")


urlpatterns = route.urls