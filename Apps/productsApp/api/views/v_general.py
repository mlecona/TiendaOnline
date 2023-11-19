from Apps.baseApp.api import GeneralListApiView

#Serializers
from Apps.productsApp.api.serializers.s_general import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer


class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer


class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer
