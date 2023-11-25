from Apps.productsApp.models import MeasureUnit, CategoryProduct, Indicator

from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    """ Unidades de Medida """
    class Meta:
        model = MeasureUnit 
        exclude = ('state', 'create_date', 'deleted_date', 'modified_date',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
        }


class CategoryProductSerializer(serializers.ModelSerializer):
    """ Categoría de Productos """
    class Meta:
        model = CategoryProduct
        exclude = ('state',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
        }


class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicator
        exclude = ('state',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'descount_value': instance.descount_value,
            'category_product': instance.category_product,
        }
