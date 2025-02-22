from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet
from django.urls import path
from .views import lista_pessoas

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]


urlpatterns += [
    path('pessoas/', lista_pessoas, name='lista_pessoas'),
]