from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import *

@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def login(req):
    if req.method == 'POST':
        return user_login(req)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def logout(req):
    if req.method == 'GET':
        return user_logout(req)
    
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def signup(req):
    if req.method == 'POST':
        return user_signup(req)
    