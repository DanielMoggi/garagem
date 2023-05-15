from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Marca, Veiculo, Modelo
from garagem.serializers import (
    AcessorioSerializer,
    CategoriaSerializer,
    CorSerializer,
    MarcaSerializer,
    ModeloSerializer,
    ModeloDetailSerializer,
    ModeloListSerializer,
    VeiculoSerializer,
    VeiculoListSerializer,
    VeiculoDetailSerializer
)

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    
class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ModeloListSerializer
        elif self.action == "retrieve":
            return ModeloDetailSerializer
        return ModeloSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()

    serializer_classes = {
        "list": VeiculoListSerializer,
        "retrieve": VeiculoDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, VeiculoSerializer)