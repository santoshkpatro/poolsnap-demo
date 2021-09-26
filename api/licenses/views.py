from rest_framework import generics, permissions
from licenses.models import License
from .serializers import LicenseSerializer


class LicenceList(generics.ListAPIView):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.licenses.all()
