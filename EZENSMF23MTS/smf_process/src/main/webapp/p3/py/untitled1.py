import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 이미지 크기 설정
image_width, image_height = 293, 218

# 데이터셋 저장 경로 설정
dataset_dir = "C:\\Users\\KiMu\\Desktop\\훈련용포스트잇"

# 데이터 전처리 함수
def preprocess_image(image):
    # 이미지 배열 복사
    image = np.array(image)
    # 이미지 크기 조정
    image = tf.image.resize(image, (image_height, image_width))
    # 픽셀 값을 0과 1 사이로 정규화
    image = image / 255.0
    return image

# 데이터셋 로드 및 전처리
datagen = ImageDataGenerator(preprocessing_function=preprocess_image)
train_data = datagen.flow_from_directory(
    dataset_dir,
    target_size=(image_height, image_width),
    batch_size=32,
    class_mode='binary'
)
