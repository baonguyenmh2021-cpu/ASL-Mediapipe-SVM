<div align="center">

# 🤟 ASL Recognition System
### **Real-time Sign Language Translation with MediaPipe & SVM**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-v0.10-teal?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.7-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)

*Một giải pháp Computer Vision gọn nhẹ, tối ưu hóa cho hiệu suất cao trên mọi thiết bị.*

---
[ 🎬 Xem Demo ] | [ 📊 Kết quả ] | [ 🛠️ Cài đặt ] | [ 🤝 Liên hệ ]
</div>

## 📖 Giới thiệu (Overview)
Dự án tập trung vào việc thu hẹp khoảng cách giao tiếp bằng cách nhận diện các chữ cái trong Ngôn ngữ Ký hiệu Mỹ (ASL). 

> **Tại sao lại dùng SVM thay vì Deep Learning?**
> Thay vì "đốt" tài nguyên vào các mô hình CNN nặng nề, chúng tui sử dụng **Feature Engineering** để trích xuất 21 điểm khớp tay. Điều này giúp hệ thống đạt tốc độ xử lý gần như tức thời (Low Latency) ngay cả trên các thiết bị không có GPU.


## ✨ Tính năng nổi bật
* **🎯 Độ chính xác cao:** Sử dụng SVM với tối ưu hóa siêu tham số (Grid Search).
* **⚡ Tốc độ vượt trội:** Trích xuất đặc trưng bằng MediaPipe giúp giảm tải xử lý ảnh thô.
* **⌨️ Bộ gõ thông minh:** * **Majority Voting:** Lọc nhiễu kết quả từ 10 frame liên tiếp.
    * **Dwell Time:** Thanh tiến trình (Progress Bar) xác nhận gõ chữ khi giữ tay ổn định.
    * **Chức năng:** Hỗ trợ phím ảo `Space` và `Delete`.

---

## 📂 Cấu trúc Thư mục
| Thư mục | Chức năng |
| :--- | :--- |
| `src/` | Chứa toàn bộ mã nguồn xử lý, huấn luyện và ứng dụng. |
| `data/` | Lưu trữ dữ liệu thô (ảnh) và dữ liệu đã qua xử lý (CSV). |
| `models/` | Nơi lưu trữ "bộ não" của hệ thống (`.pkl`). |
| `results/` | Các biểu đồ đánh giá Confusion Matrix và Heatmap. |

---

## 📊 Dữ liệu (Dataset)
Do dung lượng bộ dữ liệu gốc lên đến **3GB**, chúng tui chỉ lưu trữ các đặc trưng đã trích xuất (`.csv`) trên Repository này.

1.  **Nguồn:** [ASL Alphabet Dataset (Kaggle)](https://www.kaggle.com/datasets/grassknoted/asl-alphabet)
2.  **Cấu trúc:** Giải nén 29 thư mục chữ cái (A-Z, Del, Nothing, Space) vào `data/raw/`.

---

## 🚀 Hướng dẫn Sử dụng (Pipeline)

### 1️⃣ Thiết lập môi trường
```bash
pip install -r requirements.txt
2️⃣ Trích xuất & Huấn luyệnĐể xây dựng lại mô hình từ đầu, hãy chạy theo thứ tự:Bash# Bước 1: Quét ảnh và trích xuất tọa độ
python src/collect_landmarks.py

# Bước 2: Huấn luyện mô hình SVM
python src/train_model.py
3️⃣ Chạy ứng dụng Real-timeBashpython src/app.py
📈 Kết quả thực nghiệmMetricGiá trịAccuracy (Test Set)~99%FPS (Webcam)30+Các biểu đồ chi tiết (Confusion Matrix) có thể tìm thấy trong thư mục /results.🤝 Tác giả (Authors)Đơn vị: Trường Đại học Sư phạm - Đại học Đà Nẵng (UED)
