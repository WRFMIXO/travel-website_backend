from urllib import request
from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.utils.encoding import smart_str

from .serializers import CreateUserSerializer, ListUsersSerializer
from .models import CustomUser

# Your Views Here

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user.is_connected = True  # Mettre à jour l'état de connexion de l'utilisateur
            user.last_login = timezone.now()  # Mettre à jour la date de dernière connexion
            user.save()
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_staff': user.is_staff,
                'connected': user.is_connected,
                'profil': smart_str(user.photo),
                # Ajoutez d'autres données utilisateur si nécessaire
            }
            return Response({'message': 'Connexion réussie', 'user': user_data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Identifiant ou mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)


# Logout View
class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        if user.is_authenticated:
            user.is_connected = False
            user.save()

            logout(request)

            response = HttpResponse()
            
            response.delete_cookie('sessionid', 'csrftoken')

            return Response({'message': 'Déconnecté avec succès'}, status=status.HTTP_200_OK)
        else :
            return Response({'message': 'Aucun utilisateur connecté'}, status=status.HTTP_400_BAD_REQUEST)
    
# Créations Views
    
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer

# Listing Views
    #List All Users
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListUsersSerializer

    #List Active Users
class ActiveUsersListView(generics.ListAPIView):
    queryset = CustomUser.objects.all().filter(is_connected=True)
    serializer_class = ListUsersSerializer

    #List Inactive Users
class InactiveUsersListView(generics.ListAPIView):
    queryset = CustomUser.objects.all().filter(is_connected=False)
    serializer_class = ListUsersSerializer

    #List Admin Users
class AdminUsersListView(generics.ListAPIView):
    queryset = CustomUser.objects.all().filter(is_staff=True)
    serializer_class = ListUsersSerializer

# Updates Views
    
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListUsersSerializer

class UserDetailsView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListUsersSerializer
    
# Delete Views
    
class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListUsersSerializer
