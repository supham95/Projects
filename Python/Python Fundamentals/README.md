# Test Grade Calculator

## Project Description
Trong dự án này, bạn cần viết một chương trình để tính toán điểm thi cho nhiều lớp với sĩ số hàng nghìn học sinh. Mục đích của chương trình giúp giảm thời gian chấm điểm. Bạn sẽ áp dụng các functions (hàm) khác nhau trong Python để viết chương trình với các tác vụ sau: 

* Mở các tập tin văn bản bên ngoài được yêu cầu với exception-handling
* Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng
* Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubric) được cung cấp và báo cáo
* Tạo tập tin kết quả được đặt tên thích hợp

## How to Install and Run the Project

## Pipeline 

1. Tải các tệp dữ liệu về 1 folder trên máy tính của bạn.
2. Thực hiện các yêu cầu (tasks) của dự án

## Datasets

## How to Use the Project
**Task 1.**

1.1. Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)

1.2. Viết một chương trình cho phép người dùng nhập tên của một tệp và truy cập đọc.

1.3. Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ.

1.4. Sử dụng try/except để thực hiện việc này (đừng chỉ sử dụng một loạt câu lệnh “if” — chúng tôi muốn chương trình này càng “chung chung” càng tốt).

**Task 2:**

* Tiếp theo, bạn sẽ cần phân tích dữ liệu có trong tệp bạn vừa mở để đảm bảo rằng nó ở đúng định dạng. Mỗi tệp dữ liệu chứa một loạt câu trả lời của học sinh ở định dạng sau:

`N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D`

hoặc

`N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,`

* Giá trị đầu tiên là số ID của sinh viên. 25 chữ cái sau là câu trả lời của học sinh cho kỳ thi. Tất cả các giá trị được phân tách bằng dấu phẩy. Nếu không có chữ cái nào sau dấu phẩy, điều này có nghĩa là học sinh đã bỏ qua việc trả lời câu hỏi.

* Lưu ý rằng một số dòng dữ liệu có thể bị hỏng! Ví dụ: dòng dữ liệu này không có đủ câu trả lời:

`N12345678,B,A,D,D,C,B`

* Và dòng dữ liệu này có quá nhiều câu trả lời:

`N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D,A,B,C,D,E`

* Nhiệm vụ của bạn cho phần này của chương trình là thực hiện như sau:

2.1. Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp.

2.2. Báo cáo tổng số dòng dữ liệu không hợp lệ trong tệp.

* Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy
* N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số.

2.3. Nếu một dòng dữ liệu không hợp lệ, bạn nên báo cáo cho người dùng bằng cách in ra một thông báo lỗi. 

**Task 3:**

* Tiếp theo, bạn sẽ viết một chương trình để chấm điểm các bài thi cho một phần nhất định. Kỳ thi gồm 25 câu hỏi, trắc nghiệm. Đây là một chuỗi đại diện cho các câu trả lời:

`answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"`

Chương trình của bạn nên sử dụng những câu trả lời này để tính điểm cho mỗi dòng dữ liệu hợp lệ. Điểm có thể được tính như sau:

* +4 điểm cho mỗi câu trả lời đúng
* 0 điểm cho mỗi câu trả lời bị bỏ qua
* -1 điểm cho mỗi câu trả lời sai

Bạn cũng sẽ muốn tính toán các thống kê sau cho từng lớp:

3.1. Đếm số lượng học sinh đạt điểm cao (>80).

3.2. Điểm trung bình.

3.3. Điểm cao nhất.

3.4. Điểm thấp nhất.

3.5. Miền giá trị của điểm (cao nhất trừ thấp nhất).

3.6. Giá trị trung vị (Sắp xếp các điểm theo thứ tự tăng dần. Nếu # học sinh là số lẻ, bạn có thể lấy giá trị nằm ở giữa của tất cả các điểm (tức là [0, 50, 100] — trung vị là 50). Nếu # học sinh là chẵn bạn có thể tính giá trị trung vị bằng cách lấy giá trị trung bình của hai giá trị giữa (tức là [0, 50, 60, 100] — giá trị trung vị là 55)).

3.7. Trả về các câu hỏi bị học sinh bỏ qua nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh bỏ qua -  tỉ lệ bị bỏ qua (nếu có cùng số lượng cho nhiều câu hỏi bị bỏ thì phải liệt kê ra đầy đủ).

3.8. Trả về các câu hỏi bị học sinh sai qua nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh trả lời sai - tỉ lệ bị sai (nếu có cùng số lượng cho nhiều câu hỏi bị sai thì phải liệt kê ra đầy đủ).

* Lưu ý: các giá trị số thực làm tròn 3 chữ số thập phân

**Task 4:**

* Cuối cùng, yêu cầu chương trình của bạn tạo một tệp “kết quả” chứa các kết quả chi tiết cho từng học sinh trong lớp của bạn. Mỗi dòng của tệp này phải chứa số ID của học sinh, dấu phẩy và sau đó là điểm của họ. Bạn nên đặt tên tệp này dựa trên tên tệp gốc được cung cấp — ví dụ: nếu người dùng muốn phân tích “class1.txt”, bạn nên lưu trữ kết quả trong tệp có tên “class1_grades.txt”.

**Task 5:** Chỉ sử dụng pandas và numpy khi bạn triển khai task 1 đến task 4.

## Reference source

## Contributors

## Contact Information
* Email: *phamcongsu95@gmail.com*

