import os
from .base import *

# TODO: 테스트 DB 연결 정보 추가
DATABASES = {
    'default': {
        'ENGINE': '',
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
ALLOWED_HOSTS = ['localhost', '127.0.0.1'] # TODO: 테스트 서버 API 도메인 주소 추가하기

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