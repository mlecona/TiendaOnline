from django.urls import path
from Apps.productsApp.api.views.v_general import MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView
from Apps.productsApp.api.views.v_product import (
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    path('', ProductListCreateAPIView.as_view(), name='product_create'),
    path('retrieve-update-destroy/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve-update-destroy'),
]
