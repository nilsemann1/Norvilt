from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer


class RegisterView(generics.GenericAPIView):
    """View for registering users"""

    # Defining which serializer to send data to
    serializer_class = RegisterSerializer
    permission_classes = []

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        # If data sent to serializer is valid, then save the user
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {
            'success': True,
            'message': 'User created successfully',
            'data': serializer.data
        }

        return Response(data=response, status=status.HTTP_201_CREATED)

