
from rest_framework import routers
from product.views import ProductView

router = routers.DefaultRouter()
router.register(r'^product', ProductView, basename='product-crud')

# urlpatterns = []
urlpatterns = router.urls
