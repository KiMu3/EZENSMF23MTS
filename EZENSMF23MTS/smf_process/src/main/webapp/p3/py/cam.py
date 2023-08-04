import cv2
from pyzbar import pyzbar

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미합니다. 다른 카메라를 사용하는 경우 해당 카메라 번호를 입력하세요.

while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()

    # 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # QR 코드 및 바코드 인식
    decoded_objects = pyzbar.decode(gray)

    # 인식된 QR 코드 또는 바코드 정보 출력
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        print("인식된 코드: ", data)

        # QR 코드 주변에 사각형 그리기
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        n = len(hull)
        for j in range(0, n):
            cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # 화면에 비디오 프레임 출력
    cv2.imshow('Video', frame)

    # 종료 조건 (q 키를 누르면 종료)
    if cv2.waitKey(1) == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
