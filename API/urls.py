from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


from cliente.views import CadastrarClienteView

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
  
  
schema_view = get_schema_view(
   openapi.Info(
      title="API integration SEFAZ",
      default_version='v1',
      description="Essa API disponibiliza os documentos emitidos contra o CPF ou CNPJ do contribuinte.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@wjsolucoes.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

app_name = "Api Notas"
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/', permanent=True)),
    path('api/clientes/', include('cliente.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/token/', TokenObtainPairView.as_view()),
    path('api-auth/token/refresh', TokenRefreshView.as_view()),
    path(r'api/cadastrar_cliente',CadastrarClienteView.as_view(), name='download'),

    path(r'playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Api Notas'                   
admin.site.index_title = 'Api Notas'                 
admin.site.site_title = 'Api Notas'