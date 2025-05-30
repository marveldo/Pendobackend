from rest_framework_simplejwt.serializers import TokenObtainSerializer,AuthenticationFailed
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class CustomTokenObtainPair(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data =  super().validate(attrs)

        if self.user.is_superuser is not True :
            raise AuthenticationFailed(
                detail = 'Not a SuperUser',
                code= 403
            )

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        

        return data
    
class Userserializer(serializers.ModelSerializer):

    class Meta :

        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

