<div align="center">

# 🤟 ASL Recognition - Machine Learning Pipeline
### **Real-time American Sign Language Translation using MediaPipe & SVM**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-v0.10-00C853?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.7-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](https://github.com/baonguyenmh2021-cpu)

*Một giải pháp Computer Vision tối ưu, tốc độ cao, nhận diện ngôn ngữ ký hiệu ngay trên trình duyệt/webcam.*

---
[ 📑 Tổng quan ] | [ 📁 Cấu trúc ] | [ 🚀 Cài đặt ] | [ 📊 Kết quả ] | [ 🤝 Tác giả ]
</div>

## 📖 1. Giới thiệu (Overview)
Dự án tập trung vào việc xây dựng hệ thống nhận diện 26 chữ cái tiếng Anh trong Ngôn ngữ Ký hiệu Mỹ (ASL). 

Thay vì sử dụng các mô hình Deep Learning (CNN) nặng nề, hệ thống được tối ưu hóa qua quy trình **Feature Engineering**:
* **Trích xuất:** Sử dụng MediaPipe để lấy 21 tọa độ điểm khớp tay (x, y, z).
* **Chuẩn hóa:** Thuật toán dịch tâm giúp nhận diện linh hoạt dù tay ở bất kỳ vị trí nào.
* **Phân loại:** Mô hình SVM đạt độ chính xác ~99% trên tập Test và cực kỳ nhẹ trên CPU.



---

## ✨ 2. Tính năng nổi bật
* **⚡ Real-time Processing:** Xử lý 30+ khung hình/giây trên CPU thường.
* **🛡️ Noise Filtering:** Thuật toán **Majority Voting** (Hàng đợi 10 frames) giúp kết quả không bị nhảy chữ liên tục.
* **⌛ Dwell Time Logic:** Thanh tiến trình (Progress Bar) trực quan giúp người dùng biết khi nào chữ cái được xác nhận.
* **⌨️ Virtual Keyboard:** Hỗ trợ phím chức năng ảo như `Space` (khoảng cách) và `Delete` (xoá chữ).

---

## 📁 3. Cấu trúc Thư mục (Project Anatomy)
```text
asl-recognition/
├── data/
│   ├── raw/                # ⚠️ Dataset 3GB (Đã chặn bởi .gitignore)
│   └── processed/          # File CSV tọa độ sau khi "ép mỡ"
├── models/                 # Chứa Model SVM (.pkl) & Scaler
├── results/                # Biểu đồ Confusion Matrix & Heatmap
├── src/                    # Mã nguồn cốt lõi
│   ├── collect_landmarks.py # [BƯỚC 1] Trích xuất ảnh -> CSV
│   ├── train_model.py       # [BƯỚC 2] Huấn luyện & Tối ưu SVM
│   ├── app.py               # [BƯỚC 3] Ứng dụng Real-time
│   └── get_versions.py      # Công cụ kiểm tra môi trường
├── requirements.txt        # Danh sách thư viện cài đặt
└── README.md               # Tài liệu dự án
🚀 4. Hướng dẫn Sử dụng (Pipeline)🔹 Bước 1: Chuẩn bị môi trườngCài đặt chính xác các phiên bản thư viện đã được kiểm nghiệm:Bashpip install -r requirements.txt
🔹 Bước 2: Trích xuất đặc trưng (Feature Extraction)Script này sẽ quét qua hàng ngàn tấm ảnh để lấy tọa độ xương tay:Bashpython src/collect_landmarks.py
🔹 Bước 3: Huấn luyện mô hình (Training)Tự động tìm kiếm bộ tham số tốt nhất (Grid Search) và lưu model:Bashpython src/train_model.py
🔹 Bước 4: Chạy ứng dụng (Inference)Trải nghiệm hệ thống nhận diện thực tế qua Webcam:Bashpython src/app.py
📈 5. Kết quả thực nghiệmDự án sử dụng Confusion Matrix để kiểm tra độ nhầm lẫn giữa các lớp.MetricGiá trịĐộ chính xác (Accuracy)> 99%Thời gian phản hồi< 10msDung lượng Model~2MB(Xem chi tiết biểu đồ trong thư mục /results)🤝 6. Thông tin Tác giảTrường Đại học Sư phạm - Đại học Đà Nẵng (UED) Dự án Nghiên cứu Khoa học Sinh viên - Khoa Công nghệ thông tin.
