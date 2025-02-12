from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ClienteViewSet, FuncionarioViewSet, ProdutoViewSet, FornecedorViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'fornecedores', FornecedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
