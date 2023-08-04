import os
import glob
import shutil

# 폴더 경로 설정
folder_path = "C:\\Users\\KiMu\\Desktop\\불량품 - 복사본"  # 변경하고자 하는 폴더 경로로 바꿔주세요

# 폴더 안의 모든 파일에 대해 반복
for file_path in glob.glob(os.path.join(folder_path, "*")):
    # 파일 확장자 변경
    if file_path.endswith(".png"):  # 변경하고자 하는 기존 확장자로 바꿔주세요
        new_file_path = file_path.replace(".png", ".jpg")  # 변경하고자 하는 새로운 확장자로 바꿔주세요
        shutil.move(file_path, new_file_path)

print("이미지 파일의 확장자 변경이 완료되었습니다.")
