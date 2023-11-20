from rest_framework.routers import DefaultRouter
from Apps.productsApp.api.views.v_product_viewset import ProductViewSet
from Apps.productsApp.api.views.v_general_viewset import MeasureUnitViewSet, CategoryProductViewSet, IndicatorViewSet

router = DefaultRouter()
router.register(r'productos', ProductViewSet, basename='productos')
router.register(r'measure-unit', MeasureUnitViewSet, basename='measure_unit')
router.register(r'category-product', CategoryProductViewSet, basename='category_product')
router.register(r'indicator', IndicatorViewSet, basename='indicator')

urlpatterns = router.urls
