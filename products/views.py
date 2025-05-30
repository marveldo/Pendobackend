from django.shortcuts import render
from .serializers import ProductSerializer,Products
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status , renderers
from rest_framework.permissions import AllowAny, IsAdminUser

# Create your views here.

class ProductView(viewsets.GenericViewSet, mixins.CreateModelMixin , mixins.ListModelMixin):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_permissions(self):
        match self.action :
            case 'list' :
                self.permission_classes = [AllowAny]
            case 'create' :
                self.permission_classes = [IsAdminUser]

        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        products = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(products , many=True)
        data = {
            'items' : serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            self.perform_create(serializer=serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

