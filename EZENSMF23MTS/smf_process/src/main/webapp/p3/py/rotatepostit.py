from PIL import Image
import os
import random
import math

# 작은 사각형 이미지와 큰 사각형 이미지 경로 설정
small_rect_path = "C:\\Users\\KiMu\\Desktop\\postint\\작은네모.jpg"
large_rect_path = "C:\\Users\\KiMu\\Desktop\\postint\\큰네모.jpg"

# 데이터셋 저장 경로 설정
dataset_dir = "C:\\Users\\KiMu\\Desktop\\훈련용포스트잇"
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# 큰 사각형 이미지 열기
large_rect_image = Image.open(large_rect_path)

def paste_small_rect_on_large_rect(small_rect_path, output_path):
    # 작은 사각형 이미지 열기 (알파 채널 정보 유지)
    small_rect_image = Image.open(small_rect_path).convert("RGBA")

    # 큰 사각형 이미지 복사
    large_rect_copy = large_rect_image.copy()

    # 큰 사각형 이미지 크기 얻기
    large_width, large_height = large_rect_copy.size

    # 작은 사각형 이미지 크기 얻기
    small_width, small_height = small_rect_image.size

    # 작은 사각형의 위치를 중앙에서 조금씩 랜덤하게 이동시키기
    max_offset_x = (large_width - small_width) // 50
    max_offset_y = (large_height - small_height) // 50

    # 랜덤한 위치에 작은 사각형 이미지를 위치시키기
    offset_x = random.randint(-max_offset_x, max_offset_x)
    offset_y = random.randint(-max_offset_y, max_offset_y)

    # 큰 사각형 중앙에 작은 사각형 이미지를 위치시키기
    center_x = large_width // 2 + offset_x
    center_y = large_height // 2 + offset_y

    # 랜덤한 각도로 작은 사각형 이미지 회전시키기
    angle = random.randint(-10, 10)
    rotated_small_rect_image = small_rect_image.rotate(angle, resample=Image.BICUBIC, expand=True)

    # 회전된 작은 사각형 이미지 크기 얻기
    rotated_width, rotated_height = rotated_small_rect_image.size

    # 회전된 작은 사각형 이미지가 큰 사각형의 경계를 벗어나지 않도록 제한
    offset_x = min(max_offset_x, max(-rotated_width // 2, min(rotated_width // 2, offset_x)))
    offset_y = min(max_offset_y, max(-rotated_height // 2, min(rotated_height // 2, offset_y)))
    center_x = large_width // 2 + offset_x
    center_y = large_height // 2 + offset_y

    # 회전된 작은 사각형 이미지를 큰 사각형 이미지에 합성
    large_rect_copy.paste(rotated_small_rect_image, (center_x - rotated_width // 2, center_y - rotated_height // 2), rotated_small_rect_image)

    # 결과 이미지 저장
    large_rect_copy.save(output_path)

# 100장의 이미지 생성
for i in range(100):
    output_image_path = os.path.join(dataset_dir, f"image_{i+1}.png")
    paste_small_rect_on_large_rect(small_rect_path, output_image_path)

print("이미지 생성 완료!")
