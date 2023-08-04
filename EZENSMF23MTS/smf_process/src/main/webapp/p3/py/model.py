import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# 이미지 크기 설정
image_width, image_height = 293, 218

# 데이터셋 저장 경로 설정
dataset_dir = "C:\\Users\\KiMu\\Desktop\\훈련용포스트잇"

# 데이터 전처리 함수
def preprocess_image(image):
    image = tf.image.resize(image, (image_height, image_width))
    image = image / 255.0
    return image

# 데이터셋 로드 및 전처리
datagen = tf.keras.preprocessing.image.ImageDataGenerator(preprocessing_function=preprocess_image)
train_data = datagen.flow_from_directory(
    dataset_dir,
    target_size=(image_height, image_width),
    batch_size=32,
    class_mode='binary'
)

# 모델 정의
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_height, image_width, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 모델 훈련
history = model.fit(train_data, epochs=10)
