# CÔNG NGHỆ PHẦN MỀM


# **SaleApp - Flask Project**

## **Giới thiệu**
SaleApp là một ứng dụng web được xây dựng bằng Flask, hỗ trợ các chức năng bán hàng trực tuyến. Dự án sử dụng cơ sở dữ liệu MySQL và tích hợp SQLAlchemy để quản lý cơ sở dữ liệu.

---

## **Hướng dẫn cài đặt**

### **1. Clone dự án từ GitHub**
Sao chép repository về máy của bạn bằng lệnh:
```bash
git clone <repository_url>
```

Điều hướng vào thư mục dự án:
```bash
cd saleapp
```

---

### **2. Tạo và kích hoạt môi trường ảo**
#### **Trên Windows**
Tạo môi trường ảo:
```bash
python -m venv .venv
```

Kích hoạt môi trường ảo:
```bash
.venv\Scripts\activate
```

#### **Trên Linux/MacOS**
Tạo môi trường ảo:
```bash
python3 -m venv .venv
```

Kích hoạt môi trường ảo:
```bash
source .venv/bin/activate
```

---

### **3. Cài đặt các thư viện cần thiết**
Cài đặt các thư viện từ tệp `requirements.txt`:
```bash
python -m pip install -r requirements.txt
```

Nếu chưa có tệp `requirements.txt`, cài đặt thủ công các thư viện cần thiết:
```bash
pip install flask flask_sqlalchemy pymysql
```

Sau đó, đóng gói lại dependencies để tạo tệp `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

### **4. Cấu hình cơ sở dữ liệu**
- Mở file `app/__init__.py` và cập nhật thông tin kết nối MySQL:
  ```python
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<host>/<database>'
  ```
  - Thay `<username>`, `<password>`, `<host>`, và `<database>` bằng thông tin cụ thể của bạn.

- Đảm bảo cơ sở dữ liệu MySQL đã được khởi tạo và có quyền truy cập.

---

### **5. Chạy ứng dụng**
Chạy ứng dụng Flask:
```bash
python app/index.py
```

Ứng dụng sẽ chạy trên địa chỉ: [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Hướng dẫn làm việc với GitHub**

### **1. Kiểm tra trạng thái dự án**
Kiểm tra trạng thái các thay đổi trong dự án:
```bash
git status
```

### **2. Thêm thay đổi vào staging area**
Thêm toàn bộ thay đổi:
```bash
git add .
```

Hoặc thêm một file cụ thể:
```bash
git add <file_name>
```

### **3. Commit thay đổi**
Lưu lại thay đổi với một thông điệp:
```bash
git commit -m "Mô tả thay đổi của bạn"
```

### **4. Đẩy thay đổi lên GitHub**
Đẩy các thay đổi lên repository:
```bash
git push origin <branch_name>
```

### **5. Lấy thay đổi mới nhất từ GitHub**
Cập nhật dự án của bạn với các thay đổi mới nhất từ repository:
```bash
git pull origin <branch_name>
```

---

## **Ghi chú**
- Luôn kích hoạt môi trường ảo trước khi cài đặt thư viện hoặc chạy ứng dụng.
- Sau khi cài đặt thêm thư viện mới, hãy cập nhật `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```

---

## **Liên hệ**
- **Nguyen Phong Phu**  
  - Email: [npphus@gmail.com](mailto:npphus@gmail.com)  
  - GitHub: [github.com/fongfus](https://github.com/fongfus)

---
