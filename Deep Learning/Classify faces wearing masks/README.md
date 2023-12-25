## Mô tả dự án
* Chúng ta có một vấn đề cần phải giải quyết: 
+ Yêu cầu bộ phận phát triển hệ thống camera cung cấp những tấm ảnh có gương mặt của người đeo và không đeo khẩu trang. 
+ Sau đó chúng ta sẽ dựa trên những tấm ảnh này để đưa ra sự đoán rằng khuôn mặt của người trong một tấm ảnh hay camera bất kỳ có đang đeo khẩu trang hay không.

* Dựa trên thông tin đó, chúng ta có thể thấy rằng chúng ta đang giải quyết vấn đề phân loại, 
* Cụ thể là phân loại nhị phân (binary classification): đưa ra một đầu vào bao gồm các tấm ảnh dưới dạng dữ liệu số, trả về dự đoán có đeo khẩu trang hay không như một đầu ra. 
* Lần này, chúng ta sẽ kết hợp nhiều tập dữ liệu trên Kaggle (hoặc nguồn khác) thành một tập dữ liệu duy nhất. 
* Sử dụng hệ số ROC-AUC giữa giá trị dự đoán và giá trị được quan sát thực làm chỉ số đo sự sai lệch, chúng ta muốn chỉ số này gần bằng 1 càng tốt. 
* Chúng ta cũng sẽ kết hợp thêm mô hình nhận diện gương mặt vào mô hình phân loại này để có thể đưa ra dự đoán chính xác hơn

Trong dự án này, bao gồm những công việc sau:
* Tải các nguồn dữ liệu từ trên mạng và gộp lại thành một tập dữ liệu duy nhất.
* Xử lý các dữ liệu hình ảnh.
* Mã hóa nhãn của dữ liệu.
* Chia tập dữ liệu thành các tập huấn luyện và kiểm định.
* Xây dựng mô hình học sâu gồm nhiều lớp khác nhau.
* Huấn luyện mô hình.
* Sử dụng các mô hình nhận diện gương mặt để trích xuất gương mặt và sau đó phân loại gương mặt.
* Chạy mô hình và đánh giá dự đoán trên tập test.
