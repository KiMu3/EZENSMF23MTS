import cv2
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# 모델 로드
model = load_model("D:\\KiMu\\WorkSpace\\TeamProject\\model.h5")

# 이미지 크기 설정
image_width, image_height = 293, 218

# 카메라 캡처 준비
cap = cv2.VideoCapture(0)

while True:
    # 카메라로부터 이미지 캡처
    ret, frame = cap.read()
    
    # 캡처한 이미지 전처리
    image = Image.fromarray(frame)
    image = image.resize((image_width, image_height))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    
    # 모델로 이미지 판별
    prediction = model.predict(image)
    if prediction[0][0] >= 0.5:
        result = "good"
    else:
        result = "defective"
    
    # 이미지에 판별 결과 표시
    cv2.putText(frame, result, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # 이미지 출력
    cv2.imshow('Camera', frame)
    
    # q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
