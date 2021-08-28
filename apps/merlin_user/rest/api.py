from rest_framework import generics, mixins
from rest_framework.response import Response
from apps.merlin_user.models import MerlinUser
from apps.merlin_user.rest.serializers import UserSerializer, UserDetailSerializer

class MerlinUserViewSet(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = MerlinUser.objects.all()
    lookup_field = "code"
    lookup_url_kwarg = "user_code"
    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer = UserDetailSerializer(instance=instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def get(self, request, *args, **kwargs):
        if self.lookup_url_kwarg in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)