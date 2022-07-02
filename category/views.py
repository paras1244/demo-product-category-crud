
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Category
from .serializers import CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]        # default permission is : DjangoModelPermissionsOrAnonReadOnly
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
