from rest_framework.views import APIView
from .serializer import RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


#RegistrationView

class RegisterView(APIView):
    def post(self,request):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#Login view

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    
    
