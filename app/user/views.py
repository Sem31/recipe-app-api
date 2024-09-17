"""
Views for the user api
"""

from rest_framework import generics
# from rest_framework.views import viewsets

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """User viewset"""
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
