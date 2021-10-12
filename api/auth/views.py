from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserLoginSerializer


@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(data={'detail': 'email id or password entered in invalid'}, status=status.HTTP_404_NOT_FOUND)
