""" API de Usuario """

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Modelos
from Apps.usuariosApp.models import User
# Serializadores
from Apps.usuariosApp.api.serializers.s_user import UserSerializer, UserListSerializer #, TestUserSerializer


@api_view(['GET','POST'])
def user_api_view(request):
    
    # List
    if request.method == 'GET':
        # queryset
        users = User.objects.all().values('id', 'name', 'username', 'email', 'password')
        user_serializer = UserListSerializer(users, many = True)
        """
        # forma en que valida datos es Serializador
        test_data = {
            'name': 'develop',
            'email': 'develop@gmail.com'
        }
        test_user = TestUserSerializer(data = test_data, context = test_data)
        if test_user.is_valid():
            user_instance = test_user.save()
            print("Paso validaciones")
        else:
            print(test_user.errors)
        """
        return Response(user_serializer.data, status = status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        
        # validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario Creado Correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk=None):
    # Consulta
    users = User.objects.filter(id = pk).first()
    # Validación
    if users:
        # retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(users)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(users, data = request.data)
            #user_serializer = TestUserSerializer(users, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':
            users.delete()
            return Response({'message':'Usuario Eliminado Correctamente!'}, status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado Usuario'}, status = status.HTTP_400_BAD_REQUEST)