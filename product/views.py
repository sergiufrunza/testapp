
from rest_framework.permissions import *
from rest_framework.generics import *
from .models import *
from .serializers import *


class ProductAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerView
    permission_classes = (IsAuthenticatedOrReadOnly ,)


class ProductAPIListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerView
    permission_classes = (IsAuthenticatedOrReadOnly ,)


class ProductAPIDestroy(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerView
    permission_classes = (IsAdminUser ,)


class ProductAPIUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerUpdate
    permission_classes = (IsAdminUser ,)


class ProductAPICreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerCreate
    permission_classes = (IsAdminUser ,)



