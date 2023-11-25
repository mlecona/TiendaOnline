from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema


#Serializers
from Apps.productsApp.api.serializers.s_general import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer

class MeasureUnitViewSet(viewsets.GenericViewSet):
    """ Unidades de Medida """
    
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnitSerializer.Meta.model.objects.filter(state = True)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    @extend_schema(responses=MeasureUnitSerializer)
    def list(self, request):
        """ Listado de Unidades """
        
        measureunit_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(measureunit_serializer.data, status=status.HTTP_200_OK)


class CategoryProductViewSet(viewsets.GenericViewSet):
    """ Categorías de Productos """

    serializer_class = CategoryProductSerializer
    queryset = CategoryProductSerializer.Meta.model.objects.filter(state = True)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    @extend_schema(responses=CategoryProductSerializer)
    def list(self, request):
        """ Listado Categorías de Productos """
        
        categoryproduct_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(categoryproduct_serializer.data, status=status.HTTP_200_OK)


class IndicatorViewSet(viewsets.GenericViewSet):
    """ Indicadores de Productos """
    
    serializer_class = IndicatorSerializer
    queryset = IndicatorSerializer.Meta.model.objects.filter(state = True)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    @extend_schema(responses=IndicatorSerializer)
    def list(self, request):
        """ Listado Indicadores de Productos """
        
        indicator_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(indicator_serializer.data, status=status.HTTP_200_OK)