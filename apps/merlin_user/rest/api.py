from rest_framework import generics, permissions
from rest_framework.response import Response
from apps.merlin_user.models import MerlinUser
from apps.merlin_user.rest.serializers import UserSerializer, UserDetailSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView



class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class MerlinUserViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = MerlinUser.objects.all()
    
    def get(self, request, *args, **kwargs):
        user=request.user
        serializer = UserDetailSerializer(instance=user)
        return Response(serializer.data)
