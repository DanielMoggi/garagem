from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Marca, Veiculo, Modelo
from garagem.serializers import (
    AcessorioSerializer
    )

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

