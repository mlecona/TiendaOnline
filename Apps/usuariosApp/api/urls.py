""" Rutas de Usuarios """

from django.urls import path
from Apps.usuariosApp.api.api import user_api_view, user_detail_view


urlpatterns = [
    path('', user_api_view, name="usuario_api_view"),
    path('<int:pk>', user_detail_view, name="usuario_detail_api_view"),
]
