<div align="center">

# 🤟 ASL Recognition System
### **Real-time American Sign Language Translation with MediaPipe & SVM**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-v0.10-00C853?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.7-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

*Dự án nghiên cứu tối ưu hóa nhận diện cử chỉ tay dành cho máy cấu hình thấp.*

---
</div>

## 📖 1. Tổng quan Dự án (Overview)
Dự án tập trung vào việc xây dựng hệ thống nhận diện 26 chữ cái tiếng Anh trong Ngôn ngữ Ký hiệu Mỹ (ASL) thời gian thực. Thay vì sử dụng Deep Learning nặng nề, hệ thống sử dụng quy trình **Feature Engineering** để đạt tốc độ xử lý gần như tức thời.


---

## 📂 2. Cấu trúc Thư mục (Project Anatomy)
Để giữ cho dự án chuyên nghiệp và dễ bảo trì, cấu trúc được phân bổ như sau:

```text
asl-recognition/
├── data/
│   ├── processed/          # File CSV tọa độ (Dữ liệu đã ép mỡ)
│   └── raw/                # Dataset 3GB (Đã chặn bởi .gitignore)
├── models/                 # Chứa Model SVM (.pkl) & Scaler
├── results/                # Biểu đồ Confusion Matrix & Heatmap
├── src/                    # Mã nguồn chính
│   ├── app.py              # 🚀 Ứng dụng Real-time (Webcam)
│   ├── collect_landmarks.py # 🛠️ Bước 1: Trích xuất tọa độ
│   ├── train_model.py      # 🧠 Bước 2: Huấn luyện SVM
│   └── get_versions.py     # 🔍 Kiểm tra môi trường
├── requirements.txt        # Danh sách thư viện
└── README.md               # Tài liệu dự án
🚀 3. Hướng dẫn Sử dụng (Pipeline)Bước 1: Cài đặt môi trườngMở Terminal và chạy lệnh sau để cài đặt thư viện:Bashpip install -r requirements.txt
Bước 2: Trích xuất đặc trưngQuét ảnh trong data/raw/ và chuyển đổi thành tọa độ (x, y, z):Bashpython src/collect_landmarks.py
Bước 3: Huấn luyện mô hìnhSử dụng Grid Search để tìm bộ tham số tối ưu và lưu model:Bashpython src/train_model.py
Bước 4: Chạy ứng dụngBật Webcam để trải nghiệm hệ thống nhận diện thực tế:Bashpython src/app.py
📈 4. Kết quả thực nghiệmMô hình SVM được tối ưu hóa cho kết quả cực kỳ ấn tượng trên tập dữ liệu thử nghiệm.Chỉ số (Metric)Kết quả (Result)Độ chính xác (Accuracy)~99%Độ trễ (Latency)< 10ms (Real-time)Dung lượng Model~2MB (Siêu nhẹ)🤝 5. Thông tin Tác giảĐơn vị: Trường Đại học Sư phạm - Đại học Đà Nẵng (UED)Khoa: Công nghệ thông ti
