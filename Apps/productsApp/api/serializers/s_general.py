from Apps.productsApp.models import MeasureUnit, CategoryProduct, Indicator

from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    """ Unidades de Medida """
    class Meta:
        model = MeasureUnit 
        exclude = ('state', 'create_date', 'deleted_date', 'modified_date',)

class CategoryProductSerializer(serializers.ModelSerializer):
    """ Categoría de Productos """
    class Meta:
        model = CategoryProduct
        exclude = ('state',)

class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicator
        exclude = ('state',)
