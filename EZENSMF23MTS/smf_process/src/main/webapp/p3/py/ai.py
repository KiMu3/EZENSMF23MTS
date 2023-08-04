import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 데이터셋 경로 설정

dataset_dir = "C:\\Users\\KiMu\\Desktop\\훈련용포스트잇"
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)


train_dir = "C:\\Users\\KiMu\\Desktop\\훈련용포스트잇\\양품1"
val_dir = "C:\\Users\\KiMu\\Desktop\\훈련용포스트잇\\불량품1"

# 이미지 크기와 배치 크기 설정
image_size = (293, 218)
batch_size = 32

# 데이터 생성기 설정
train_datagen = ImageDataGenerator(rescale=1.0/255)
val_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='binary'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='binary'
)

# 모델 설계
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 모델 학습
epochs = 10
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=val_generator,
    validation_steps=val_generator.samples // batch_size,
    epochs=epochs
)

# 학습 결과 평가
loss, accuracy = model.evaluate(val_generator)
print("평가 결과 - Loss: {:.4f}, Accuracy: {:.4f}".format(loss, accuracy))
