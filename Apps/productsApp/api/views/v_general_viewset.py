from rest_framework import viewsets

#Serializers
from Apps.productsApp.api.serializers.s_general import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer

class MeasureUnitViewSet(viewsets.GenericViewSet):
    """ Unidades de Medida """
    
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnitSerializer.Meta.model.objects.filter(state = True)


class CategoryProductViewSet(viewsets.GenericViewSet):
    """ Categorías de Productos """

    serializer_class = CategoryProductSerializer
    queryset = CategoryProductSerializer.Meta.model.objects.filter(state = True)


class IndicatorViewSet(viewsets.GenericViewSet):
    """ Indicadores de Productos """
    
    serializer_class = IndicatorSerializer
    queryset = IndicatorSerializer.Meta.model.objects.filter(state = True)
