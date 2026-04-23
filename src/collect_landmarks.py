import cv2
import mediapipe as mp
import os
import pandas as pd


RAW_DATA_PATH = "../data/asl_alphabet_train/asl_alphabet_train"

PROCESSED_DIR = "../data/processed"
CSV_FILENAME = "asl_data_balanced_final.csv"

TARGET_SAMPLES = 1255  


os.makedirs(PROCESSED_DIR, exist_ok=True)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.3)

print(f"⚖️ BẮT ĐẦU TRÍCH XUẤT & CÂN BẰNG DỮ LIỆU (Target: {TARGET_SAMPLES} mẫu/lớp)...")

# Kiểm tra xem có thư mục raw không
if not os.path.exists(RAW_DATA_PATH):
    print(f"❌ Lỗi: Không tìm thấy thư mục {RAW_DATA_PATH}!")
    print("Hãy tạo thư mục 'data/raw' ở ngoài thư mục gốc và bỏ các thư mục ảnh (A, B, C...) vào đó.")
    exit()

labels = sorted([d for d in os.listdir(RAW_DATA_PATH) if os.path.isdir(os.path.join(RAW_DATA_PATH, d))])
if not labels:
    print(f"❌ Thư mục {RAW_DATA_PATH} đang trống! Vui lòng cho ảnh vào trước khi chạy.")
    exit()

all_data = []

# Quét từng thư mục nhãn (A, B, C...)
for label in labels:
    label_path = os.path.join(RAW_DATA_PATH, label)
    img_list = os.listdir(label_path)
    success_count = 0

    for img_name in img_list:
        if success_count >= TARGET_SAMPLES: 
            break  

        # Xử lý đặc biệt cho lớp 'nothing'
        if label == 'nothing':
            all_data.append([0.0] * 63 + [label])
            success_count += 1
            continue

        img_path = os.path.join(label_path, img_name)
        img = cv2.imread(img_path)
        
        if img is None: 
            continue

        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # CHUẨN HÓA DỊCH TÂM (Trừ đi tọa độ gốc của cổ tay)
                base_x = hand_landmarks.landmark[0].x
                base_y = hand_landmarks.landmark[0].y
                base_z = hand_landmarks.landmark[0].z

                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x - base_x, lm.y - base_y, lm.z - base_z])

                all_data.append(landmarks + [label])
                success_count += 1

    print(f"✅ Lớp {label}: Thu được {success_count} mẫu chuẩn.")

# Đóng MediaPipe giải phóng RAM
hands.close()


print("\n💾 Đang đóng gói dữ liệu vào file CSV...")
cols = [f'c{i}' for i in range(63)] + ['label']
df = pd.DataFrame(all_data, columns=cols)

csv_path = os.path.join(PROCESSED_DIR, CSV_FILENAME)
df.to_csv(csv_path, index=False)

print(f"🎉 HOÀN TẤT! Đã lưu tổng cộng {len(df)} mẫu 'sạch' vào: {csv_path}")
print("Bây giờ bạn có thể xóa thư mục 'data/raw' cho nhẹ máy và chạy file 'train_model.py'!")
