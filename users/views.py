from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPair, User,Userserializer
from rest_framework import generics, mixins , status , renderers
from rest_framework.response import Response


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPair

class UserView(generics.GenericAPIView , mixins.ListModelMixin , mixins.CreateModelMixin):

    queryset = User.objects.all()
    serializer_class = Userserializer
    renderer_classes = [renderers.JSONRenderer]

    def get(self, request , *args , **kwargs):
        return self.list(request, *args , **kwargs)
    
    def post(self, request, *args , **kwargs):
        return self.create(request, *args , **kwargs)
    
    def list(self, request, *args, **kwargs):
        users = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(users , many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer=serializer)
        return Response(serializer.data , status=status.HTTP_201_CREATED)