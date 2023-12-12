import logging
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import authenticate

from models.users.serializers import UserSerializer

from apps.common.decorators.exception_decorator import exception


logger = logging.getLogger("mylogger")

@exception("") 
def user_login(req):
    user = authenticate(
        username=json.loads(req.body)['username'], 
        password=json.loads(req.body)['password']
    )
    if user is not None:
        serializer = UserSerializer(user)
        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        response = Response(
            {
                "user": serializer.data,
                "message": "login success",
                "token": {
                    "access": access_token,
                    "refresh": refresh_token
                }
            },
            status=status.HTTP_200_OK
        )

        response.set_cookie("access", access_token, httponly=True)
        response.set_cookie("refresh", refresh_token, httponly=True)
        return response
    return Response(status=status.HTTP_400_BAD_REQUEST)

def user_logout(req):
    response = Response({
        "message": "logout success"
    }, status=status.HTTP_202_ACCEPTED)
    response.delete_cookie("access")
    response.delete_cookie("refresh")
    return response    

def user_signup(req):
    serializer = UserSerializer(data=json.loads(req.body))
    if serializer.is_valid():
        user = serializer.save()

        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        response = Response({
            "user": serializer.data,
            "message": "Signup success",
            "token": {
                "access": access_token,
                "refresh": refresh_token
            },
        },
        status=status.HTTP_200_OK
        )

        response.set_cookie("access", access_token, httponly=True)
        response.set_cookie("refresh", refresh_token, httponly=True)

        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)