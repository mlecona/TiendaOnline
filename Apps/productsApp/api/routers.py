from rest_framework.routers import DefaultRouter
from Apps.productsApp.api.views.v_product_viewset import ProductViewSet

router = DefaultRouter()
router.register(r'productos', ProductViewSet, basename='productos')

urlpatterns = router.urls
