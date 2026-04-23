🤟 ASL Recognition - MediaPipe & SVM Pipeline
Dự án Hệ thống Nhận diện Ngôn ngữ Ký hiệu Mỹ (ASL) thời gian thực. > Một sản phẩm nghiên cứu ứng dụng Computer Vision và Machine Learning tối ưu cho thiết bị cấu hình thấp.

📑 Tổng quan Dự án (Overview)
Dự án này giải quyết bài toán nhận diện các chữ cái trong bảng chữ cái ASL thông qua Webcam.

Thay vì sử dụng các mô hình Deep Learning (CNN) nặng nề, dự án đi theo hướng Feature Engineering:

Sử dụng MediaPipe để trích xuất 21 điểm mốc xương bàn tay (Hand Landmarks).

Dùng mô hình SVM (Support Vector Machine) để phân loại tọa độ.

Kết quả: Hệ thống cực nhẹ, độ chính xác cao và đạt tốc độ xử lý gần như tức thời trên CPU.

🛠️ Công nghệ Sử dụng (Tech Stack)
Ngôn ngữ: Python 3.10+

Thị giác máy tính: OpenCV, MediaPipe

Học máy (ML): Scikit-learn (SVM), Pandas, Numpy

Đánh giá: Matplotlib, Seaborn

📁 Cấu trúc Thư mục (Directory Structure)
Plaintext
asl-recognition/
├── data/
│   └── processed/          # File asl_data_balanced_final.csv (Sau khi ép mỡ)
├── models/                 # Lưu trữ asl_model_final.pkl & asl_scaler.pkl
├── results/                # Các biểu đồ đánh giá (Confusion Matrix,...)
├── src/                    # Mã nguồn chính
│   ├── collect_landmarks.py # Bước 1: Trích xuất tọa độ từ ảnh
│   ├── train_model.py       # Bước 2: Huấn luyện & Tối ưu mô hình
│   ├── app.py               # Bước 3: Chạy ứng dụng Real-time
├── requirements.txt        # Danh sách thư viện cần thiết
└── README.md               # Tài liệu hướng dẫn dự án
📊 Nguồn Dữ liệu (Dataset)
Lưu ý quan trọng: Bộ dữ liệu gốc có dung lượng khoảng 3GB nên đã được cấu hình trong .gitignore để không lưu trữ trực tiếp trên Repository này nhằm đảm bảo hiệu suất tải.

Tải về: Bạn có thể tải bộ dữ liệu chính thức tại ASL Alphabet Dataset trên Kaggle.
Link: https://www.kaggle.com/datasets/grassknoted/asl-alphabet

Cài đặt: Giải nén và đặt các thư mục chữ cái (A, B, C...) vào đường dẫn: data/.

🚀 Hướng dẫn Cài đặt & Sử dụng
1. Cài đặt môi trường
Mở Terminal và chạy lệnh sau để cài đặt chính xác các phiên bản thư viện đã được Tech Lead kiểm nghiệm:

Bash
pip install -r requirements.txt
2. Quy trình thực thi (Pipeline)
Giai đoạn 1: Trích xuất tọa độ (Feature Extraction)
Quét toàn bộ ảnh trong data/raw/, chuyển đổi thành tọa độ (x, y, z) và lưu vào file CSV.

Bash
cd src
python collect_landmarks.py
Giai đoạn 2: Huấn luyện mô hình (Model Training)
Đọc dữ liệu từ CSV, thực hiện Grid Search để tìm siêu tham số tốt nhất cho SVM và lưu mô hình.

Bash
python train_model.py
Giai đoạn 3: Trải nghiệm ứng dụng (Real-time App)
Bật Webcam và bắt đầu nhận diện chữ cái kèm theo thanh tiến trình xác nhận (Dwell Time).

Bash
python app.py
📈 Kết quả & Đánh giá
Mô hình được đánh giá qua Confusion Matrix để đảm bảo không bị nhầm lẫn giữa các chữ cái có hình dáng gần giống nhau (như M, N, T). Các báo cáo chi tiết được xuất tự động vào thư mục results/.

🤝 Liên hệ & Đóng góp
Tác giả: Trần Thị Bảo Nguyên (Tech Lead)

Đơn vị: Trường Đại học Sư phạm - Đại học Đà Nẵng (UED)
