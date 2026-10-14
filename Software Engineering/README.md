# Software Engineering (Kỹ thuật Phần mềm)
**International School – Vietnam National University, Hanoi (VNU-IS)**  
*Khoa Công nghệ Ứng dụng & Khoa học Máy tính*

---

## 🎯 Giới thiệu môn học
Môn học **Software Engineering** cung cấp kiến thức nền tảng và chuyên sâu về quy trình phát triển phần mềm hiện đại, phương pháp mô hình hóa hướng đối tượng chuẩn hóa bằng **UML (Unified Modeling Language)**, và các mẫu thiết kế hướng đối tượng kinh điển (**GoF Design Patterns**).

Sinh viên được rèn luyện kỹ năng phân tích bài toán thực tế, thiết kế kiến trúc phần mềm có tính mở rộng cao, giảm thiểu ghép nối lỏng (*loose coupling*), tăng cường tính kết nối nội tại (*high cohesion*), đồng thời hiện thực hóa bằng mã nguồn có cấu trúc chuẩn mực.

---

## 📚 Danh sách các Assignment / Tutorial

### 1. [Assignment 1: UML Modeling](Assigment1/assigment1-group2.ipynb)
- **Tài liệu gốc:** `Tutorial1_UML_Modeling.pdf` (TS. Hà Mạnh Hùng)
- **Chủ đề chính:**
  - **Exercise 1: Adapter Design Pattern** - Tích hợp thư viện đồ họa ngoài `SVGWriter` vào hệ thống vẽ hình học `MoteurRendu` (PDF, PNG, SVG).
  - **Exercise 2: Composite Design Pattern** - Thiết kế và duyệt cấu trúc cây đối tượng đa cấp với `Element`, `Noeud`, và `Feuille`. Phân tích giải thuật duyệt tiền thứ tự (Pre-order DFS).
  - **Exercise 3: Hệ thống xác thực người dùng** - Phân tích kiến trúc 3 lớp (`IULogin`, `GestionnairePersonne`, `Personne`), xây dựng Activity Diagram quy trình đăng nhập và Object Diagram thực thi.
- **Sản phẩm bàn giao:**
  - File sơ đồ Draw.io hoàn chỉnh: [`assigment1_all_diagrams.drawio`](Assigment1/assigment1_all_diagrams.drawio)
  - Master Notebook kèm Output: [`assigment1-group2.ipynb`](Assigment1/assigment1-group2.ipynb)
  - Thư mục mã nguồn: [`exercise1/`](Assigment1/exercise1/), [`exercise2/`](Assigment1/exercise2/), [`exercise3/`](Assigment1/exercise3/)

---

### 2. [Assignment 2: The Design Patterns](Assigment2/assigment2-group2.ipynb)
- **Tài liệu gốc:** `Sujet_TD3_en_VNUIS.pdf` (TS. Hà Mạnh Hùng)
- **Chủ đề chính:**
  - **Exercise 1: Singleton Design Pattern** - Giải quyết bài toán lãng phí bộ nhớ khi tạo nhiều logger trong các tài khoản ngân hàng `CompteBancaire`. Thiết kế lớp `Journalisation` theo mẫu Singleton để dùng chung một thể hiện duy nhất toàn cục.
  - **Exercise 2: Decorator Design Pattern** - Khắc phục nhược điểm bùng nổ số lượng lớp (Class Explosion) do đa kế thừa bằng cách ứng dụng Decorator Pattern để bọc động các chức năng định dạng HTML (`HTMLLogger`) và mã hóa ký tự (`EncryptLogger`) lên các đích ghi log (`ConsoleLogger`, `FileLogger`).
- **Sản phẩm bàn giao:**
  - File sơ đồ Draw.io hoàn chỉnh: [`assigment2_all_diagrams.drawio`](Assigment2/assigment2_all_diagrams.drawio)
  - Master Notebook kèm Output: [`assigment2-group2.ipynb`](Assigment2/assigment2-group2.ipynb)
  - Thư mục mã nguồn: [`exercise1/`](Assigment2/exercise1/), [`exercise2/`](Assigment2/exercise2/)

---

## 🛠️ Công nghệ & Công cụ sử dụng
- **Ngôn ngữ lập trình:** Python 3 (Object-Oriented Programming & Type Hinting)
- **Mô hình hóa UML:** StarUML, Diagrams.net / Draw.io (Class, Sequence, Object, Activity Diagrams)
- **Môi trường thực thi & Báo cáo:** Jupyter Notebook (`.ipynb`), Matplotlib (UML High-Resolution Renderers)
