from produto.viewsets import ProdutoViewSet, CadastrarProdutoViewSet

from rest_framework.routers import DefaultRouter

route = DefaultRouter()

route.register(r'cadastrar', CadastrarProdutoViewSet, basename="cadastar_produto")
route.register(r'show_produtos', ProdutoViewSet, basename="produtos")


urlpatterns = route.urls