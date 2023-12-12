import os
import boto3

from PIL import Image
from io import BytesIO

from config.secret_info import s3_info
from django.conf import settings

from apps.common.decorators.exception_decorator import exception

# secret info로 옮기기, 프로덕트나 테스트면 os에서, 개발모드면 secret info에서 가져오게
KEY_ID = ''
KEY = ''
REGION = 'ap-northeast-2'

'''
AWS S3 버킷 경로 조회
'''
@exception("S3 버킷 경로 조회 에러", return_value=None)
def getS3Path(mode):
    return s3_info.bucket[mode]


'''
AWS S3 버킷에서 파일 다운로드
'''
@exception("S3 파일 다운로드 에러", return_value=None)
def S3download(key_value, mode):
    if not os.path.isdir(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)
    client = boto3.client("s3", aws_access_key_id=KEY_ID, aws_secret_access_key=KEY, region_name=REGION)
    name = key_value[key_value.rfind("/"):]
    client.download_file(s3_info.bucket[mode], key_value, settings.MEDIA_ROOT+name)

'''
AWS S3 버킷에서 이미지 읽기
'''
@exception("S3 이미지 읽기 에러", return_value=None)
def S3ImageOpen(file_key, mode):
    client = boto3.client("s3", aws_access_key_id=KEY_ID, aws_secret_access_key=KEY, region_name=REGION)
    response = client.get_object(Bucket=s3_info.bucket[mode], Key=file_key)

    img_data = response["Body"].read()
    return Image.open(BytesIO(img_data))

'''
AWS S3 버킷에서 파일 읽어서 반환
'''
@exception("S3 파일 읽기 에러", return_value=None)
def S3FileOpen(file_key, mode):
    client = boto3.client("s3", aws_access_key_id=KEY_ID, aws_secret_access_key=KEY, region_name=REGION)
    response = client.get_object(Bucket=s3_info.bucket[mode], Key=file_key)

    file_content = response["Body"].read()
    return file_content