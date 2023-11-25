from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

# Serializador
from Apps.usuariosApp.api.serializers.s_user import UserTokenSerializer


class UserToken(APIView):

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(user = 
                UserTokenSerializer().Meta.model.objects.filter(username = username).first())
            return Response({'token': user_token.key}, 
                                    status = status.HTTP_200_OK)
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectas.'}, 
                                    status = status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = 
                                request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user'] # type: ignore
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({'token': token.key, 
                                    'user': user_serializer.data,
                                    'message': 'Inicio de sesión Exitoso.'}, 
                        status = status.HTTP_200_OK)
                else:
                    """
                    all_sessions = Session.objects.filter(expire_date_gte = datetime.now)
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token, created = Token.objects.get_or_create(user = user)
                    user_serializer = UserTokenSerializer(user)
                    return Response({'token': token.key, 
                                    'user': user_serializer.data,
                                    'message': 'Inicio de sesión Exitoso.'}, 
                        status = status.HTTP_200_OK)
                    """
                    token.delete()
                    return Response({'error': 'Ya se inicio sesión con este usuario.'}, 
                                status = status.HTTP_409_CONFLICT)
            else:
                return Response({'error': 'Este usuario no puede iniciar sesión.'}, 
                                status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrecto.'}, 
                            status = status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'Hola desde response'}, 
                        status = status.HTTP_200_OK)

class Logout(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            token = request.POST.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user
                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')): # type: ignore
                            session.delete()

                token.delete()

                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return Response({'token eliminado': token_message, 'session message': session_message}, 
                            status = status.HTTP_200_OK)
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales.'}, 
                            status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado en la petición.'}, 
                            status = status.HTTP_409_CONFLICT)
