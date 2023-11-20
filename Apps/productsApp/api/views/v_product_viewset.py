""" Aplicación de Productos"""

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from Apps.productsApp.api.serializers.s_producto import ProductSerializer

class ProductViewSet(viewsets.GenericViewSet):
    """ Clase Para Procesar Productos """
    
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state = True)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        """ Listado de Productos """
        
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """ Creación de nuevos Productos """
        
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto Creado Correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """ Actualización de Productos existentes """
        if self.get_queryset(pk):
            # send information to serializer reference instance
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data) 
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """ Eliminación de Productos """
        
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
