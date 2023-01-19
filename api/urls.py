from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
  
  
schema_view = get_schema_view(
   openapi.Info(
      title="API BRASILPREV",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

app_name = "API BRASILPREV"

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/', permanent=True)),

    path('api/cliente/', include('cliente.urls'), name='cliente'),
    path('api/produto/', include('produto.urls'), name='produto'),
    path('api/plano/', include('plano.urls'), name='plano'),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/token/', TokenObtainPairView.as_view(), name="token_view"),
    path('api-auth/token/refresh', TokenRefreshView.as_view(), name="token_refresh_view"),

    path(r'playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'API BRASILPREV'        
admin.site.index_title = 'API BRASILPREV'                 
admin.site.site_title  = 'API BRASILPREV'