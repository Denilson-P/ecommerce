from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ClientViewSet, ProductViewSet, SaleViewSet, AvaliationViewSet


router = SimpleRouter()
router.register("client", ClientViewSet)
router.register("product", ProductViewSet)
router.register("sale", SaleViewSet)
router.register("avaliation", AvaliationViewSet)

urlpatterns = router.urls
