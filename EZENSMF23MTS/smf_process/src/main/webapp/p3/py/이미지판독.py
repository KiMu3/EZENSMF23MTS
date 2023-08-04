from PIL import Image
import numpy as np

# 테스트 이미지 경로
test_image_path = "C:\\Users\\KiMu\\Desktop\\불량품\\불량2 (9).png"

# 테스트 이미지 로드 및 전처리
test_image = Image.open(test_image_path)
test_image = test_image.resize((image_width, image_height))
test_image = np.array(test_image) / 255.0
test_image = np.expand_dims(test_image, axis=0)

# 모델로 테스트 이미지 판별
prediction = model.predict(test_image)
if prediction[0][0] >= 0.5:
    print("양품입니다.")
else:
    print("불량품입니다.")
