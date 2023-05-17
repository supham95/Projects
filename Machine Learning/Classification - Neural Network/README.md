# Predicting the likelihood of developing type 2 diabetes in Arizona

## Project Description
Pima là một nhóm người Mỹ bản địa sống ở Arizona. Nhờ yếu tố di truyền mà nhóm người này có thể tồn tại bình thường với chế độ ăn ít carbohydrat trong nhiều năm. Trong những năm gần đây, sự thay đổi đột ngột từ cây nông nghiệp truyền thống sang thực phẩm chế biến sẵn, cùng với việc giảm các hoạt động thể chất, đã khiến họ có tỷ lệ mắc bệnh tiểu đường loại 2 tăng cao. Và vì lý do này, họ trở thành đối tượng của nhiều cuộc nghiên cứu.

Project này sẽ xây dựng mô hình phân loại để dự đoán khả năng mắc bệnh tiểu đường loại 2 tại Arizona.

## How to Install and Run the Project
1. Tải các tệp từ phần Tài nguyên về kho lưu trữ của bạn (driver hoặc trên máy tính).

2. Bạn mở tệp notebook bằng Jupyter Notebook, Google Colab hoặc bất cứ môi trường nào để có thể chạy tệp notebook.

3. Cài đặt các thư viện cần thiết có trong bài:
* pandas
* numpy
* matplotlib
* seaborn
* mpl_toolkits
* sklearn

## Pipeline 

1. Đọc dữ liệu.

3. Trực quan dữ liệu.

4. Tiền xử lý dữ liệu.

5. Xây dựng mô hình phân loại và đánh giá chất lượng.
* KNN
* Decision Tree
* SVM
* Logistic Regression
* Neural Network

6. Xây dựng mô hình phân loại bằng Ensemble và đánh giá chất lượng.
* Soft voting
* Hard voting

7. Đưa ra kết quả tổng hợp chất lượng mô hình phân loại của tất cả thuật toán.

## Datasets

Tập dữ liệu gồm dữ liệu từ 768 phụ nữ với 8 đặc điểm, cụ thể:

* Số lần mang thai
* Nồng độ đường huyết sau 2 giờ trong xét nghiệm dung nạp glucose đường uống
* Huyết áp tâm trương (mm Hg)
* Độ dày của nếp gấp da (mm)
* Insulin huyết thanh trong 2 giờ (mu U/ml)
* Chỉ số BMI (trọng lượng tính bằng kg/(chiều cao tính bằng m)^2)
* Chức năng phả hệ bệnh tiểu đường
* Tuổi (năm)
* Cột cuối cùng của tập dữ liệu cho biết một người có bị chẩn đoán mắc bệnh tiểu đường (1) hay không (0)

## How to Use the Project
**Task 1.** Đọc dữ liệu

* Thêm tên cột vào dữ liệu đã đọc
* Gợi ý: Sử dụng phương thức read_csv của Pandas

**Task 2.** Tính ma trận tương quan cho tập dữ liệu

**Task 3.** Trực quan ma trận tương quan bằng heatmap trong seaborn

**Task 4.** Trực quan histogram với tất cả cột tập dữ liệu

**Task 5.** Gán giá trị bị khuyết trên 'BMI', 'BloodP', 'PlGlcConc', 'SkinThick', 'TwoHourSerIns' bằng giá trị trung vị hoặc bất kỳ cách nào khác có hiệu quả

**Task 6.** Thực hiện co giãn dữ liệu thành giá trị trung bình bằng 0 và phương sai bằng 1

* Lưu ý: Chỉ áp dụng với các đặc trưng, không áp dụng với mục tiêu.

**Task 7.** Tách tập dữ liệu train/test data.

* test site = 20%
* random_state=7

**Task 8.** In ra tỷ lệ dương tính trên tổng số phụ nữ mắc bệnh tiểu đường trong tập dữ liệu đầy đủ, tập huấn luyện và tập kiểm tra

**Task 9.** Xây dựng mô hình KNN để dự đoán mục tiêu
* Tinh chỉnh siêu tham số để có được mô hình KNN với độ chính xác tốt nhất.
* In ra các giá trị siêu tham số của mô hình KNN với độ chính xác tốt nhất.
* Đưa ra dự đoán từ dữ liệu huấn luyện và kiếm tra trên mô hình KNN.
* Tính f1 score và Jaccard score rồi lưu vào f1_scores dict và jaccard_scores dict.
* Trả lời câu hỏi.

*Yêu cầu:*
* Số lượng siêu tham số tối thiểu: 3
* Số lượng giá trị siêu tham số tối đa trong một lần tìm kiếm: 20
* Sử dụng GridSearchCV trong sklearn.model_selection.
* Không nên sử dụng dữ liệu kiểm tra để tìm ra các tham số tốt nhất.
* F1 score trên dữ liệu kiểm tra phải cao hơn 0.6, Jaccard score phải cao hơn 0.4.

**Task 10.** Xây dựng mô hình Decision Tree để dự đoán mục tiêu

* Thực hiện tương tự Task 9

**Task 11.** Xây dựng mô hình Support Vector Machine để dự đoán mục tiêu

* Thực hiện tương tự Task 9

**Task 12.** Xây dựng mô hình Logistic Regression để dự đoán mục tiêu

* Thực hiện tương tự Task 9

**Task 13.** Xây dựng mô hình Neural Network để dự đoán mục tiêu

* Thực hiện tương tự Task 9

**Task 14.** Xây dựng mô hình Soft Voting Ensemble để dự đoán mục tiêu

* Điều chỉnh trọng số trong Soft Voting Ensemble để đưa ra kết quả dự đoán tốt nhất.
* Đưa ra dự đoán từ dữ liệu huấn luyện và kiếm tra trên mô hình soft voting ensembling model.
* Tính f1 score và Jaccard score rồi lưu vào f1_scores dict và jaccard_scores dict.

*Yêu cầu:*
* Sử dụng 5 mô hình trên đã xây dựng
* Sử dụng cùng một thiết lập cho 5 mô hình như các bước trên.
* F1 score trên dữ liệu kiểm tra phải lớn hơn 0.66, Jaccard similarity score phải lớn hơn 0.5.

**Task 15.** Xây dựng mô hình Hard Voting Ensemble để dự đoán mục tiêu

* Thực hiện tương tự Task 14

*Yêu cầu:*
* F1 score trên dữ liệu kiểm tra phải lớn hơn 0.57, Jaccard similarity score phải lớn hơn 0.45.

**Task 16.** Tạo dataframe mô tả kết quả chính xác như trên

## Reference source

## Contributors

## Contact Information
* Email: *phamcongsu95@gmail.com*
