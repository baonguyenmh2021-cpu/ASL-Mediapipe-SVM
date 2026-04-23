<div align="center">

# 🤟 ASL Recognition System
### 🚀 Real-time American Sign Language Translation (CPU-Optimized)

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/MediaPipe-Google-green?style=for-the-badge&logo=google"/>
<img src="https://img.shields.io/badge/Scikit--Learn-SVM-orange?style=for-the-badge&logo=scikit-learn"/>
<img src="https://img.shields.io/badge/Performance-30FPS-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Model_Size-~2MB-blueviolet?style=for-the-badge"/>

<br>

🔥 **Fast. Lightweight. Real-time. No GPU required.**

</div>

---

## 🧠 Problem

Nhận diện ngôn ngữ ký hiệu thường phụ thuộc vào Deep Learning (CNN, LSTM) →  
❌ Nặng  
❌ Chậm  
❌ Cần GPU  

👉 Không phù hợp cho **real-time trên máy yếu**.

---

## 💡 Solution

Xây dựng hệ thống nhận diện ASL dựa trên:

- **Feature Engineering** thay vì Deep Learning
- **MediaPipe** → trích xuất 21 keypoints bàn tay
- **SVM (Support Vector Machine)** → phân loại nhanh, nhẹ

👉 Kết quả:  
⚡ **Real-time 30+ FPS trên CPU**  
⚡ **Độ chính xác ~99%**  
⚡ **Model chỉ ~2MB**

---

## ⚙️ System Pipeline

```mermaid
graph LR
A[Input Image] --> B[MediaPipe Hand Detection]
B --> C[Extract 21 Landmarks]
C --> D[Normalize Coordinates]
D --> E[SVM Model]
E --> F[Predicted Character]
✨ Key Features
⚡ High Performance
30+ FPS trên CPU (không cần GPU)
Latency < 10ms
🛡️ Noise Reduction
Majority Voting (10 frames)
Giảm rung & sai lệch prediction
⏳ Smart Input (Dwell Time)
Giữ tay → xác nhận ký tự
Tránh nhập nhầm
⌨️ Virtual Keyboard
Space → khoảng trắng
Delete → xóa ký tự
📂 Project Structure
asl-recognition/
│
├── data/
│   ├── raw/               # Dataset gốc (~3GB)
│   └── processed/         # CSV landmarks
│
├── models/                # SVM model + scaler
├── results/               # Confusion Matrix, Heatmap
│
├── src/
│   ├── app.py             # 🎯 Real-time app
│   ├── collect_landmarks.py  # 📊 Feature extraction
│   ├── train_model.py     # 🧠 Training + GridSearch
│   └── utils.py
│
├── requirements.txt
└── README.md
🚀 Getting Started
1. Install dependencies
pip install -r requirements.txt
2. Extract Features
python src/collect_landmarks.py
3. Train Model
python src/train_model.py
4. Run Real-time App
python src/app.py
📊 Results
Metric	Value
Accuracy	> 99%
Latency	< 10ms
FPS	30+
Model Size	~2.1 MB
📸 Demo (Recommended thêm video/GIF ở đây)

👉 Bạn nên thêm:

GIF demo webcam
hoặc video YouTube
🧩 Tech Stack
Python
MediaPipe (Hand Tracking)
Scikit-learn (SVM)
OpenCV (Real-time Processing)
🎯 Why This Project Stands Out

✔ Không dùng Deep Learning nhưng vẫn đạt accuracy cao
✔ Tối ưu cho CPU → thực tế hơn
✔ Có UX (progress bar, keyboard) → không chỉ model

👉 Đây là điểm mà nhà tuyển dụng rất thích:

“Bạn hiểu bài toán, không chỉ biết dùng CNN”

🤝 Author

Nguyen Bao

💻 AI / Computer Vision Enthusiast
🎯 Focus: Real-time Systems & Optimization
⭐ Future Improvements
Thêm word prediction (NLP)
Hỗ trợ câu thay vì ký tự
Deploy Web (Streamlit / Flask)
Mobile version
