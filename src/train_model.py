import os
import pandas as pd
import numpy as np
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

DATA_PATH = "../data/asl_data_balanced_final.csv" 
MODEL_DIR = "../models"
RESULTS_DIR = "../results"

# Tự động tạo thư mục nếu máy người khác chưa có
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ==========================================
# GIAI ĐOẠN 1: ĐỌC VÀ CHUẨN BỊ DỮ LIỆU
# ==========================================
print("⏳ Đang tải dữ liệu...")
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    print(f"❌ Lỗi: Không tìm thấy file tại {DATA_PATH}.")
    print("Hãy chắc chắn bạn đang chạy code từ thư mục 'src' và đã chạy file trích xuất!")
    exit()

X = df.drop('label', axis=1)
y = df['label']

# Chia 80% Train / 20% Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Chuẩn hóa thang đo (Cực kỳ quan trọng với SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n🚀 Đang huấn luyện Baseline Model...")
model = SVC()
model.fit(X_train_scaled, y_train)
y_pred_base = model.predict(X_test_scaled)

print("📊 BÁO CÁO KẾT QUẢ MÔ HÌNH CƠ BẢN (BASELINE):")
print(classification_report(y_test, y_pred_base))

param_grid = {'C': [1, 10, 50], 'gamma': ['scale', 0.01], 'kernel': ['rbf']}
grid = GridSearchCV(SVC(probability=True), param_grid, cv=3, verbose=2, n_jobs=-1)

print("\n🧠 Đang huấn luyện & tối ưu hóa siêu tham số (GridSearch)...")
grid.fit(X_train_scaled, y_train)

print("\n📈 Đang lưu biểu đồ Heatmap Grid Search...")
results = pd.DataFrame(grid.cv_results_)
results['param_C'] = results['param_C'].astype(float)
results['param_gamma'] = results['param_gamma'].astype(str)

scores_matrix = results.pivot_table(index='param_C', columns='param_gamma', values='mean_test_score')

plt.figure(figsize=(8, 6))
sns.heatmap(scores_matrix, annot=True, cmap='viridis', fmt='.4f',
            cbar_kws={'label': 'Mean Cross-Validation Accuracy'})
plt.title('Hiệu năng mô hình theo siêu tham số $C$ và $\gamma$', fontsize=14, pad=15)
plt.xlabel('Parameter: $\gamma$ (Gamma)', fontsize=12)
plt.ylabel('Parameter: $C$ (Regularization)', fontsize=12)
plt.gca().invert_yaxis()
plt.tight_layout()

# Lưu ảnh vào thư mục results thay vì hiện lên
plt.savefig(f"{RESULTS_DIR}/grid_search_heatmap.png", dpi=300)
plt.close() 

best_model = grid.best_estimator_

print(f"\n💾 Đang lưu mô hình và bộ chuẩn hóa vào '{MODEL_DIR}/'...")
joblib.dump(best_model, f"{MODEL_DIR}/asl_model_final.pkl")
joblib.dump(scaler, f"{MODEL_DIR}/asl_scaler.pkl")

y_pred_best = best_model.predict(X_test_scaled)
print("\n🔥 BÁO CÁO KẾT QUẢ MÔ HÌNH TỐI ƯU (BEST MODEL):")
print(classification_report(y_test, y_pred_best))

# Vẽ và lưu Ma trận nhầm lẫn
cm = confusion_matrix(y_test, y_pred_best)
plt.figure(figsize=(15, 12))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=grid.classes_, yticklabels=grid.classes_)
plt.title("Confusion Matrix - ASL Final Model", fontsize=16)
plt.xlabel('Predicted Label', fontsize=12)
plt.ylabel('True Label', fontsize=12)
plt.savefig(f"{RESULTS_DIR}/confusion_matrix_final.png", dpi=300)
plt.close()

print(f"\n🎉 HOÀN TẤT! File chạy đã được đóng gói chuyên nghiệp. Bạn có thể tự tin đẩy code lên GitHub.")
