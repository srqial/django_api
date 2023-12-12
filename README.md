# Django Restframework 클린 프로젝트
> Django와 DjangoRestframework 기반의 클린 프로젝트

## 버전
- Django==4.2.7
- djangorestframework==3.14.0
- mysqlclient==2.2.0

## 모드
> `config` > `settings`폴더 하위에 프로젝트 실행 설정&프로필을 구성한다.
* `base.py` : 공통 설정을 정의한다.
* `develop.py` : 개발(로컬) 설정을 정의한다.
  * DB > 개발 DB 정보를 정의한다. 
  * 로그 레벨 INFO로 설정
  * DEBUG = True
  * ALLOWED_HOSTS > localhost, 로컬 호스트 IP 정보 추가
* `test.py` : 테스트 서버 설정을 정의한다.
  * SECRET_KEY > EB에 정의하거나 프로젝트 내에 환경 변수 설정 필요
  * DB > 테스트 DB 정보를 정의한다. 
  * 로그 레벨 ERROR로 설정(default 값이므로 개발 시 상황에 따라 변경 가능)
  * DEBUG = False
  * ALLOWED_HOSTS > 로컬호스트, 테스트 서버 EB만 접근 가능하도록 EB 도메인 주소 추가
* `product.py` : 운영 서버 설정을 정의한다.
  * SECRET_KEY > EB에 정의하거나 프로젝트 내에 환경 변수 설정 필요
  * DB > 운영 DB 정보를 정의한다. 
  * 로그 레벨 ERROR로 설정(default 값이므로 개발 시 상황에 따라 변경 가능)
  * DEBUG = False(default 값이므로 개발 시 상황에 따라 변경 가능)
  * ALLOWED_HOSTS > 로컬호스트, 운영 서버 EB만 접근 가능하도록 EB 도메인 주소 추가
  
  
## 실행
![](https://imgur.com/salLVgl.png)
  * 환경변수 설정
  ![](https://imgur.com/eAOW6cx.png)
      * AWS_ACCESS_KEY_ID = #값넣기
      * AWS_SECRET_ACCESS_KEY = #값넣기
      * PYTHONUNBUFFERED=1
      * DJANGO_SETTINGS_MODULE=config.settings.develop > 개발 모드 프로필로 프로젝트 시작
      * DJANGO_SETTINGS_MODULE=config.settings.test > 테스트 모드 프로필로 프로젝트 시작
      * DJANGO_SETTINGS_MODULE=config.settings.product > 운영 모드 프로필로 프로젝트 시작
      * SECRET_KEY = #운영 모드 선택시 추가
        * SETCREY_KEY는 django 프로젝트 생성 시 최초로 생성된다.
        * 이 클린 프로젝트를 클론해서 사용할 경우 SECRET_KEY 생성이되지 않으므로, 수동으로 생성해서 사용한다.
          * 현재 프로젝트에서는 환경 변수에서 가져오거나 없을 시 생성하도록 설정함
          * 별도로 다시 생성해서 설정하고 싶은 경우 아래와 같은 방법 참고
            * 방법1: https://djecrety.ir/ -> 시크릿 키 생성기로 키를 생성해 사용
            * 방법2: 터미널에 `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`를 입력해 생성하거나, 코드 내에 삽입해서 생성할 수 있다.
![](https://imgur.com/wg9jXcv.png)


## 배포
> aws 파이프라인이용한 elasticbeanstalk 자동 배포 <br>
### 설정파일
* `.ebextensions` : 구성파일 (ec2 kst로 타임존 설정, django 설정,django 실행 모드설정) <br>
* `.platfrom` : 플랫폼 파일 (nginx 설정)
    * `/etc/nginx/conf.d/elasticbeanstalk/*.conf` >위치함
  
### eb 환경속성
* PYTHONPATH :/var/app/venv/staging-LQM1lest/bin
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* DJANGO_SETTINGS_MODULE
  *  config.settings.develop > 개발 모드 선택
  *  config.settings.test > 테스트 모드 선택
  *  config.settings.product > 운영 모드 선택
     * 운영모드시 SECRET_KEY 환경속성 추가

## 구조

```bash
Root
├─.ebextensions/
│  └─django.config
│  └─timezone.config
├─.platform
│  └─nginx
│      └─conf.d
│          └─elasticbeanstalk
│               └─00_application.conf
├─apps
│  └─사용자정의 API를 추가/
│  └─common/
│      └─decorators/
│      └─utils/
├─models/
│  └─사용자 정의 모델을 추가/
│  └─users/ # djangorestframework 기본 user 모델을 상속받아 재정의 해서 사용중(커스텀 더 필요한 부분은 재정의 추가) or 별도로 정의해도 됨
├─config/
│  └─settings/
│      └─base.py
│      └─develop.py
│      └─product.py
│  └─secret_info/
│      └─secret key, s3 등 정의
│  └─asgi.py
│  └─urls.py
│  └─wsgi.py
├─media-packages/
│  └─static/
│      └─css/
│      └─js/
│      └─font/
│      └─img/
│  └─staticfiles/
│  └─template/
```


