import os
from .base import *

# TODO: 운영 DB 연결 정보 추가
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DEBUG = False

LOGGING= {
    'version' : 1,
    'disable_existing_loggers' : False,
    'handlers' :{
        'console':{
            'class' : 'logging.StreamHandler'
        },
    },
    'formatters': {  # message 출력 포맷 형식
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers' :{
        'mylogger':{
            'handlers' : ['console'],
            'level':'ERROR' #운영모드 정의
        },
    },
}