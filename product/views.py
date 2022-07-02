from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from product.models import Product
from product.serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]        # default permission is : DjangoModelPermissionsOrAnonReadOnly
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
