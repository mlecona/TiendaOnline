""" Serializadores de Usuarios """

from rest_framework import serializers
from Apps.usuariosApp.models import User

class UserSerializer(serializers.ModelSerializer):
    """ Clase Serializadores de Usuarios """
    class Meta:
        model = User
        fields = '__all__'


    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user

    def update(self, instance, validate_data):
        update_user = super().update(instance, validate_data)
        update_user.set_password(validate_data['password'])
        update_user.save()
        return update_user


class UserListSerializer(serializers.ModelSerializer):
    """ Clase Serializadores de Usuarios """
    class Meta:
        model = User

    def to_representation(self, instance):
        return { 
            # Opción con es recomendable objects.all().values('id', 'username', 'email', 'password')
            'id': instance['id'],
            'name': instance['name'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }


"""
            # Opción con objects.all() no recomendado
            'id': instance.id,
            'Nombre_Usuario': instance.username,
            'Correo_electronico': instance.email,
            'clave': instance.password
            
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()
    
    def validate_name(self, value):
        # custom validation
        if "develop" in value:
            raise serializers.ValidationError("Error, no puede existir un usuario con este nombre")
        return value
    
    def validate_email(self, value):
        # custom validation
        if value == "":
            raise serializers.ValidationError("Error, tienen que indicar un correo")
        
        #if self.validate_name(self.context['name']) in value:
        #    raise serializers.ValidationError("Error, El email no puede contener el nombre")
        
        return value
    
    def validate(self, data):
        return data

    def create(self, validate_data):
        return self.model.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
"""