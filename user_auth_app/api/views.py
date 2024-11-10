from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from user_auth_app.models import UserProfile
from .serializer import UserProfileSerializer, RegistrationSerializer
from join_app.api.serializers import UserSerializer

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CustomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'id': user.id
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)

        # serializer = self.serializer_class(data=request.data)
        # data = {}

        # if serializer.is_valid():
        #     user = serializer.validated_data['user']
        #     token, created = Token.objects.get_or_create(user=user)
        #     data = {
        #         'token': token.key,
        #         'username': user.username,
        #         'email': user.email
        #     }
        #     return Response(data, status=status.HTTP_202_ACCEPTED)
        # else:
        #     data = serializer.errors
        #     return Response(data, status=status.HTTP_400_BAD_REQUEST)

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email,
                'id': saved_account.id
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
class UserFromTokenView(APIView):
    def post(self, request):
        token = request.data.get('token')
        if token:
            try:
                user = User.objects.get(auth_token=token)
                serializer = UserSerializer(user)
                id = serializer.data['id']
                return Response(id, status=status.HTTP_202_ACCEPTED)
            except User.DoesNotExist:
                pass
        return Response({'error': 'Token is not valid.'}, status=status.HTTP_403_FORBIDDEN)