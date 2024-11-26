from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer,UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User registred successfully'}, status= 201)
        return Response(serializer.errors, status= 400)
    
    
class UserProfileView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successfully logout'}, status = 200)
        except Exception as e:
            return Response({'error':str(e)}, status= 400)