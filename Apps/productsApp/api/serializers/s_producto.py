from rest_framework import serializers

from Apps.productsApp.models import Product
from Apps.productsApp.api.serializers.s_general import MeasureUnitSerializer, CategoryProductSerializer



class ProductSerializer(serializers.ModelSerializer):
    # 1er Forma
    #measure_unit = MeasureUnitSerializer()
    #category_product = CategoryProductSerializer()
    # 2da Forma depende de lo que se puso en str del modelo
    #measure_unit = serializers.StringRelatedField()
    #category_product = serializers.StringRelatedField()
    """
    def validate_imagen(self, imagen):
        if imagen != "":
            return imagen
        return ""
    """
    class Meta:
        model = Product
        exclude = ('state', 'create_date', 'deleted_date', 'modified_date',)

    # 3er Forma
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'imagen': instance.imagen if instance.imagen != '' else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else ''
        }
