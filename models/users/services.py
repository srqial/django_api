from .serializers import UsersSerializer
from datetime import datetime

USER_ID = 'user_id'
USERNAME = 'username'
PASSWORD = 'password'
CREATED_AT = 'created_at'

def save(username, password):
    user = {
        USERNAME: username,
        PASSWORD: password,
        CREATED_AT: datetime.now()
    }

    serializer = UsersSerializer(data=user)

    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors