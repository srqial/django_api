import io, os
from django.conf import settings

from PIL import Image
from pdf2image import convert_from_path

from apps.common.decorators.exception_decorator import exception

'''
이미지 파일 불러오기
'''
@exception("이미지 파일 열기 오류 발생", return_value=None)
def load_image(img_path):
    with io.open(img_path, "rb") as img_file:
        content = img_file.read()

    img_file = Image.open(img_path)
    width = img_file.width
    height = img_file.height

    return content, width, height

'''
이미지 자르기
'''
@exception("이미지 파일 자르기 오류 발생", return_value=None)
def crop(img, normalized_vertices):
    box = [(vertex.x * img.width, vertex.y * img.height) for vertex in normalized_vertices]
    cropped_image = img.crop((box[0][0], box[0][1], box[2][0], box[2][1]))
    return cropped_image

'''
이미지 파일 바이트로 변환
'''
@exception("이미지 파일 바이트 변환 오류 발생", return_value=None)
def img2bytes(img):
    byte_io = io.BytesIO()
    img.save(byte_io, "JPEG")
    return byte_io.getvalue()

'''
이미지 파일의 픽셀 값 계산
'''
def calculate_pixels(image):
    imgWidth, imgHeight = image.size
    return imgWidth * imgHeight

'''
pdf 파일을 이미지로 변환
'''
def pdf2img(file_name):
    pdf2img_dir = os.path.join(settings.BASE_DIR, "media_packages/pdf2img/")
    
    if not os.path.isdir(pdf2img_dir):
        os.mkdir(pdf2img_dir)

    img_name_list = []
    max_pixels = 75000000
    dpi = 200
    scale = 1
    exceeds_max_pixels = True

    while exceeds_max_pixels:
        images = convert_from_path(settings.MEDIA_ROOT + file_name, dpi=int(dpi/scale))
        image_for_scale = images[0]

        count = 0
        for image in images:       
            if calculate_pixels(image) >= max_pixels:
                count = count + 1
                if  len(images) > 1 and calculate_pixels(image) > calculate_pixels(image_for_scale):
                    image_for_scale = image

                if (calculate_pixels(image_for_scale)/max_pixels) > scale:
                    scale = calculate_pixels(image_for_scale)/max_pixels
                     
        if count == 0:
            exceeds_max_pixels = False
        
    for i, image in enumerate(images):
        img_name_list.append(pdf2img_dir + file_name + str(i) + ".jpg")
        image.save(img_name_list[i], "jpeg")
    return img_name_list

'''
파일 종류 체크
'''
@exception("파일 종류 체크 오류 발생", return_value=None)
def check_file_ext(filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    if ext == '.ppt' or ext == '.pptx':
        return 'ppt'
    elif ext == '.pdf':
        return 'pdf'
    else:
        return 'other'

def clean_local_file():
    local_path = [settings.MEDIA_ROOT, os.path.join(settings.BASE_DIR, "media_packages/pdf2img/")]
    for path in local_path:
        file_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        if file_list:
            for file in file_list:
                os.remove(os.path.join(path, file))