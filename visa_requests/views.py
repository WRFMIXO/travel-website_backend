from rest_framework.response import Response
from .serializers import RequestSerializer
from .models import VisaRequests
from rest_framework import status, generics

# Create your views here.
class CreateRequestView(generics.CreateAPIView):
    queryset = VisaRequests.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        # Vous pouvez personnaliser le comportement de perform_create() si nécessaire
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message': 'Votre demande a été validée'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': "Votre demande de visa n'a pas pu être validée"}, status=status.HTTP_400_BAD_REQUEST)
        

class ListRequestView(generics.ListAPIView):
    queryset = VisaRequests.objects.all()
    serializer_class = RequestSerializer

class UpdateRequestView(generics.RetrieveAPIView):
    queryset = VisaRequests.objects.all()
    serializer_class = RequestSerializer

class DestroyRequestView(generics.RetrieveDestroyAPIView):
    queryset = VisaRequests.objects.all()
    serializer_class = RequestSerializer

# Others Opérations
class ListRequestByUsers(generics.ListAPIView):
    serializer_class = RequestSerializer
    
    def list(self, request, *args, **kwargs):
        user_id = request.data.get('id')  # Utiliser request.data.get() pour récupérer les données
        queryset = VisaRequests.objects.filter(userConcerned=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)