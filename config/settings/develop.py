import os
from .base import *

# TODO: 개발 DB 설정 수정
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

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DEBUG = True

LOGGING= {
    'version' : 1,
    'disable_existing_loggers' : False, #디폴트 : True, 장고의 디폴트 로그 설정을 대체. / False : 장고의 디폴트 로그 설정의 전부 또는 일부를 다시 정의
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
            'level':'INFO'
        },
    },
}