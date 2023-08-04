from PIL import Image
import os
import random

# 작은 사각형 이미지와 큰 사각형 이미지 경로 설정
small_rect_path = "C:\\Users\\KiMu\\Desktop\\postint\\작은네모.jpg"
large_rect_path = "C:\\Users\\KiMu\\Desktop\\postint\\큰네모.jpg"

# 데이터셋 저장 경로 설정
dataset_dir = "C:\\Users\\KiMu\\Desktop\\훈련용포스트잇2"
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# 큰 사각형 이미지 열기
large_rect_image = Image.open(large_rect_path)

def paste_small_rect_on_large_rect(small_rect_path, output_path):
    # 작은 사각형 이미지 열기
    small_rect_image = Image.open(small_rect_path)

    # 큰 사각형 이미지 복사
    large_rect_copy = large_rect_image.copy()

    # 큰 사각형 이미지 크기 얻기
    large_width, large_height = large_rect_copy.size

    # 작은 사각형 이미지 크기 얻기
    small_width, small_height = small_rect_image.size

    # 작은 사각형의 위치를 중앙에서 조금씩 랜덤하게 이동시키기
    max_offset_x = large_width - small_width
    max_offset_y = large_height - small_height

    # 랜덤한 위치에 작은 사각형 이미지를 위치시키기
    offset_x = random.randint(-max_offset_x // 10, max_offset_x // 10)
    offset_y = random.randint(-max_offset_y // 10, max_offset_y // 10)

    # 큰 사각형 중앙에 작은 사각형 이미지를 위치시키기
    center_x = (large_width - small_width) // 2 + offset_x
    center_y = (large_height - small_height) // 2 + offset_y
    large_rect_copy.paste(small_rect_image, (center_x, center_y))

    # 결과 이미지 저장
    large_rect_copy.save(output_path)

# 100장의 이미지 생성
for i in range(100):
    output_image_path = os.path.join(dataset_dir, f"image_{i+1}.jpg")
    paste_small_rect_on_large_rect(small_rect_path, output_image_path)

print("이미지 생성 완료!")
