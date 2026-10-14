# Chương trình Đào tạo Đại học Quốc tế VNU-IS (Vietnam National University, Hanoi)
**Trường Quốc tế – Đại học Quốc gia Hà Nội**  
*Kho tổng hợp tài liệu học tập, bài tập thực hành (Tutorials/Assignments), mã nguồn và đồ án môn học.*

---

## 🏛️ Giới thiệu chung về VNU-IS
**Trường Quốc tế (VNU-IS) – ĐHQGHN** là đơn vị tiên phong trong việc đào tạo chuẩn quốc tế hoàn toàn bằng tiếng Anh. Các chương trình đào tạo tại trường trang bị cho sinh viên năng lực thực hành vững vàng, tư duy giải quyết vấn đề hệ thống, tiếp cận các công nghệ phần mềm và khoa học dữ liệu tiên tiến trên thế giới.

Repository này được tổ chức khoa học để lưu trữ các bài tập lớn, bài thực hành Lab/Tutorial của các môn học chuyên ngành công nghệ thông tin và kỹ thuật phần mềm.

---

## 📂 Danh mục các môn học & Chương trình đào tạo

| Thư mục môn học | Tên môn học | Giảng viên / Tài liệu | Nội dung trọng tâm |
| :--- | :--- | :--- | :--- |
| [📁 `Software Engineering/`](Software%20Engineering/README.md) | **Kỹ thuật Phần mềm (Software Engineering)** | TS. Hà Mạnh Hùng | - Mô hình hóa hệ thống bằng UML (Class, Sequence, Object, Activity Diagrams)<br>- Kiến trúc hướng đối tượng & GoF Design Patterns (Adapter, Composite, Singleton, Decorator)<br>- Thực hành mô phỏng mã nguồn & Jupyter Notebook báo cáo |

---

## 📋 Chi tiết môn học hiện tại: `Software Engineering`

### 1. [Assignment 1 - Tutorial 1: UML Modeling](Software%20Engineering/Assigment1/assigment1-group2.ipynb)
- **Tài liệu:** `Tutorial1_UML_Modeling.pdf`
- **Nội dung:**
  - **Exercise 1:** Adapter Pattern kết nối `SVGWriter` với bộ vẽ hình học `MoteurRendu`.
  - **Exercise 2:** Composite Pattern phân cấp cây `Element`, `Noeud`, `Feuille` và giải thuật duyệt tiền thứ tự (Pre-order DFS).
  - **Exercise 3:** Hệ thống xác thực người dùng (`IULogin`, `GestionnairePersonne`, `Personne`) kèm Activity Diagram và Object Diagram.
- **Tài nguyên:** Notebook [assigment1-group2.ipynb](Software%20Engineering/Assigment1/assigment1-group2.ipynb), file vẽ [assigment1_all_diagrams.drawio](Software%20Engineering/Assigment1/assigment1_all_diagrams.drawio).

### 2. [Assignment 2 - Tutorial 3: The Design Patterns](Software%20Engineering/Assigment2/assigment2-group2.ipynb)
- **Tài liệu:** `Sujet_TD3_en_VNUIS.pdf`
- **Nội dung:**
  - **Exercise 1:** Singleton Pattern quản lý thể hiện `Journalisation` dùng chung duy nhất cho các tài khoản ngân hàng `CompteBancaire`.
  - **Exercise 2:** Decorator Pattern mở rộng động hành vi ghi log (bọc thẻ HTML `HTMLLogger`, mã hóa xoay vòng ký tự `EncryptLogger`) mà không bị bùng nổ số lượng lớp.
- **Tài nguyên:** Notebook [assigment2-group2.ipynb](Software%20Engineering/Assigment2/assigment2-group2.ipynb), file vẽ [assigment2_all_diagrams.drawio](Software%20Engineering/Assigment2/assigment2_all_diagrams.drawio).

---

## 🚀 Hướng dẫn mở và xem các tài nguyên
1. **Xem sơ đồ UML:** Mở trực tiếp các file `.drawio` bằng trang web [draw.io (app.diagrams.net)](https://app.diagrams.net/) hoặc extension *Draw.io Integration* trên VS Code.
2. **Chạy Jupyter Notebook:**
   ```bash
   jupyter notebook "Software Engineering/Assigment1/assigment1-group2.ipynb"
   jupyter notebook "Software Engineering/Assigment2/assigment2-group2.ipynb"
   ```
3. **Chạy các script Python độc lập:**
   ```bash
   # Chạy Assignment 1
   python "Software Engineering/Assigment1/exercise1/exercise1.py"
   python "Software Engineering/Assigment1/exercise2/exercise2.py"
   python "Software Engineering/Assigment1/exercise3/exercise3.py"

   # Chạy Assignment 2
   python "Software Engineering/Assigment2/exercise1/exercise1.py"
   python "Software Engineering/Assigment2/exercise2/exercise2.py"
   ```
