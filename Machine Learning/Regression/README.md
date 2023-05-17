# Predicting the number of people admitted to American College

## Project Description

Project này sẽ áp dụng mô hình hồi quy vào bài toán thực tế để dự đoán số người trúng tuyển American College.

## How to Install and Run the Project
1. Tải các tệp liên quan về kho lưu trữ của bạn (driver hoặc trên máy tính).

2. Bạn mở tệp notebook bằng Jupyter Notebook, Google Colab hoặc bất cứ môi trường nào để có thể chạy tệp notebook.

3. Cài đặt các thư viện cần thiết có trong bài:
* pandas
* numpy
* matplotlib
* mpl_toolkits
* sklearn

## Pipeline 

1. Đọc dữ liệu.

2. Tiền xử lý dữ liệu.

3. Trực quan dữ liệu.

4. Chuẩn bị dữ liệu.

5. Xây dựng mô hình hồi quy tuyến tính đơn biến.

6. Xây dựng mô hình hồi quy tuyến tính đa biến.

7. Xây dựng mô hình hồi quy tuyến tính trên toàn bộ đặc trưng để quan sát mối quan hệ giữa các đặc trưng và mục tiêu.

8. Xây dựng mô hình Lasso để lựa chọn đặc trưng tốt nhất cho mục tiêu.

## Datasets

Dự án này liên quan đến tập dữ liệu College, trong file College.csv trong thư mục dữ liệu. Nó chứa các biến sau cho 777 trường đại học và cao đẳng khác nhau ở Mỹ:

**Private**: Chỉ báo public/private

**Apps**: Số lượng hồ sơ nhận được

**Accept**: Số lượng sinh viên được chấp thuận

**Enroll**: Số sinh viên mới đăng ký

**Top10perc**: Sinh viên mới từ top 10% lớp trung học

**Top25perc**: Sinh viên mới từ top 25% lớp trung học

**F.Undergrad**: Số sinh viên đại học toàn thời gian

**P.Undergrad**: Số sinh viên đại học bán thời gian

**Outstate**: Học phí ngoại bang

**Room.Board**: Chi phí ăn ở

**Books**: Chi phí giáo trình theo ước tính

**Personal**: Chi tiêu cá nhân theo ước tính

**PhD**: Phần trăm giảng viên có bằng Tiến sĩ

**Terminal**: Phần trăm giảng viên có Terminal degree (bẳng cấp cao nhất trong một lĩnh vực nhất định)

**S.F.Ratio**: Tỷ lệ sinh viên/giảng viên

**perc.alumni**: Phần trăm cựu sinh viên đã quyên góp

**Expend**: Chi phí giảng dạy cho mỗi sinh viên

**Grad.Rate**: Tỷ lệ tốt nghiệp

## How to Use the Project
**Task 1.** Đọc dữ liệu

* Gợi ý: Sử dụng phương thức read_csv của thư viện Pandas

**Task 2.** Mã hóa hạng mục private với phương thức map()

**Task 3.** Trực quan ma trận phương quan

* Tính ma trận trực quan
* Trực quan ma trận bằng seaborn

**Task 4.** Trực quan Scatter từng đặc trưng với mục tiêu

**Task 5.** Phân tách dữ liệu đặc trưng vào X, dữ liệu mục tiêu vào y từ dữ liệu gốc

**Task 6:** Tách dữ liệu thành train/test data

* Lưu ý: Dữ liệu train chiếm 70% và random_state là 7.

**Task 7:** Mô hình hóa hồi quy tuyến tính chi phí ăn ở và số lượng sinh viên được chấp nhận và trực quan mô hình

* Tạo dữ liệu train và test.
* Điều chỉnh hình dạng dữ liệu phù hợp với đầu vào mô hình.
* Xây dựng và huấn luyện mô hình bằng thư viện Sklearn.
* Đánh giá chất lượng mô hình trên tập test với chỉ số R2.
* Trực quan mô hình với dữ liệu test thông qua hàm có sẵn.

**Task 8:** Mô hình hóa hồi quy tuyến tính số lượng sinh viên ghi danh cho mỗi trường đại học và số lượng sinh viên được chấp nhận và trực quan mô hình

* Thực hiện tương tự với Task 7

**Task 9:** Mô hình hóa hồi quy tuyến tính từng đặc trưng với số lượng sinh viên được chấp nhận và trực quan hóa mô hình với dữ liệu test

* Thực hiện tương tự với Task 7 dựa vào vòng lặp

**Task 10:** Mô hình hóa hồi quy tuyến đa biến số lượng sinh viên ghi danh cho mỗi trường đại học và chi phí ăn ở để dự đoán số lượng sinh viên được chấp nhận và trực quan mô hình

* Thực hiện tương tự với Task 7 nhưng sử dụng 2 đặc trưng thay vì 1 đặc trưng.
* Trực quan bằng một hàm có sẵn khác phù hợp với 2 đặc trưng.

**Task 11:** Sử dụng hồi quy tuyến tính với toàn bộ đặc trưng để quan sát tác động của từng đặc trưng đến mục tiêu

* Thực hiện tương tự với Task 7 nhưng sử dụng toàn bộ đặc trưng thay vì 1 đặc trưng.
* Co giãn đặc trưng để mọi đặc trưng đều công bằng.
* Trả lời câu hỏi.

**Task 12:** Xây dựng mô hình hồi quy tuyến tính của riêng bạn

* Yêu cầu: R2 score >= 0.9.

**Task 13:** Sử dụng hồi quy Lasso để chọn ra đặc trưng tốt nhất để dự đoán số lượng sinh viên được chấp nhận

* Yêu cầu: Tìm giá trị alpha sao cho mô hình đạt R2 score >= 9.2.
* Trả lời câu hỏi.

## Reference source

## Contributors

## Contact Information
* Email: *phamcongsu95@gmail.com*

