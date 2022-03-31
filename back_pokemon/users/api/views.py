from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    # NO FUNCIONA??????????
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# _________________________________________________________________
# from users.api.serializers import HelloSerializer
#
#
# class HelloApiView(APIView):
#     serializer_class = HelloSerializer
#
#     def get(self, request, format=None):
#         an_apiview = [
#             'texto de prueba',
#             'segundo texto',
#             'tercer texto'
#         ]
#         return Response({'message': 'Hello', 'an_apiview': an_apiview})
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'hello {name}'
#             return Response({'message': message})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#
#         return Response({'method': 'PUT'})
#
#     def patch(self, request, pk=None):
#
#         return Response({'method': 'PATCH'})
#
#     def delete(self, request, pk=None):
#
#         return Response({'method': 'DELETE'})
