from django.contrib.auth.models import User, Group
from rest_framework import viewsets, parsers
from rest_framework import permissions
from FileUpload.serializers import UserSerializer, GroupSerializer, DropBoxSerializers
from .models import DropBox




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class DropBoxViewset(viewsets.ModelViewSet):
    queryset = DropBox.objects.all()
    serializer_class = DropBoxSerializers
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

