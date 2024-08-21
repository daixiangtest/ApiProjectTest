from django.shortcuts import render
from datetime import timedelta

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            res = {'token': serializer.validated_data['access'], 'refresh': serializer.validated_data['refresh']}
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(res, status=status.HTTP_200_OK)
