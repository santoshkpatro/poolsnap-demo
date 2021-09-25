from rest_framework import generics, permissions
from rights.models import Right
from .serializers import RightSerializer


class UserRightList(generics.ListAPIView):
    serializer_class = RightSerializer
    queryset = Right.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.rights.all()
