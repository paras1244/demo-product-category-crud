
from rest_framework import routers
from .views import CategoryView


router = routers.DefaultRouter()
router.register(r'^category', CategoryView, basename='category-crud')


urlpatterns = [
    
]
urlpatterns += router.urls
