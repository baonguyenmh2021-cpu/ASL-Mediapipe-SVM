import cv2
import mediapipe as mp
import joblib
import os
import numpy as np
from collections import deque


MODEL_PATH = "../models/asl_model_final.pkl"
SCALER_PATH = "../models/asl_scaler.pkl"


print("⏳ Đang khởi động hệ thống...")
try:
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise FileNotFoundError("Không tìm thấy Model hoặc Scaler. Vui lòng chạy file train_model.py trước!")
    
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("✅ Hệ thống đã sẵn sàng! Đã nạp Model và Scaler thành công.")
except Exception as e:
    print(f"❌ Lỗi: {e}")
    exit()


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)


sentence = ""  
current_label = ""  
dwell_counter = 0  
CONFIRM_FRAMES = 20  # Giữ ~0.6 giây để xác nhận gõ (30 FPS)
history_queue = deque(maxlen=10)  # Lọc nhiễu

cap = cv2.VideoCapture(0)
print("\n--- 🎬 Đang mở Webcam... Nhấn 'c' để xóa hết, 'q' để thoát ---")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    detected_label = "nothing"  

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            base_x = hand_landmarks.landmark[0].x
            base_y = hand_landmarks.landmark[0].y
            base_z = hand_landmarks.landmark[0].z
            
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x - base_x, lm.y - base_y, lm.z - base_z])

            landmarks_scaled = scaler.transform([landmarks])
            prediction = model.predict(landmarks_scaled)[0]
            history_queue.append(prediction)

            detected_label = max(set(history_queue), key=history_queue.count)

    label_lower = detected_label.lower()

    if label_lower != "nothing":
        if detected_label == current_label:
            dwell_counter += 1
        else:
            current_label = detected_label
            dwell_counter = 0

        if dwell_counter == CONFIRM_FRAMES:
            if "space" in label_lower:
                sentence += " "
            elif "del" in label_lower:
                sentence = sentence[:-1]  
            elif len(detected_label) == 1:  
                sentence += detected_label

            dwell_counter = -15
    else:
        current_label = ""
        dwell_counter = 0

    cv2.rectangle(frame, (0, 0), (640, 65), (40, 40, 40), -1)
    cv2.putText(frame, f"Text: {sentence}", (15, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 255, 255), 2)

    if dwell_counter > 0:
        bar_width = int((dwell_counter / CONFIRM_FRAMES) * 640)
        cv2.rectangle(frame, (0, 65), (bar_width, 72), (0, 255, 0), -1)

    # Trạng thái hiện tại
    status_color = (0, 255, 255) if label_lower != "nothing" else (150, 150, 150)
    cv2.putText(frame, f"Holding: {detected_label}", (15, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 1)

    cv2.imshow('ASL Smart Sentence Builder', frame)

    # --- PHÍM TẮT ---
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): break
    if key == ord('c'): sentence = ""  

cap.release()
cv2.destroyAllWindows()