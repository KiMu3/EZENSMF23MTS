from PIL import Image
import os

# 원본 이미지 파일이 있는 디렉토리
input_dir = "C:\\Users\\KiMu\\Desktop\\양품"

# 변경된 이미지 파일을 저장할 디렉토리
output_dir = "C:\\Users\\KiMu\\Desktop\\양품1"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 변경할 이미지 파일들의 확장자 (예: .jpg, .png 등)
file_extensions = ['.jpg', '.png']

# 변경할 이미지 파일의 크기
new_width, new_height = 293, 218

def resize_image(input_path, output_path, new_size):
    # 이미지 열기
    img = Image.open(input_path)

    # 이미지 크기 조정
    resized_img = img.resize(new_size)

    # 조정된 이미지 저장
    resized_img.save(output_path)

# 디렉토리 내의 모든 이미지 파일에 대해 크기 조정
for filename in os.listdir(input_dir):
    if filename.lower().endswith(tuple(file_extensions)):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        resize_image(input_path, output_path, (new_width, new_height))

print("이미지 크기 조정 완료!")
