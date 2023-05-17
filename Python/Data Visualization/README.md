# Covid-19 Data Analysis

## Project Description
**Coronavirus** là một họ vi-rút có thể gây bệnh, khiến *cảm lạnh thông thường* và *ho* trở bệnh nặng hơn. **Hội chứng hô hấp Trung Đông (MERS-CoV)** và **Hội chứng hô hấp cấp tính nặng (SARS-CoV)** là những trường hợp nghiêm trọng mà thế giới phải đối mặt.<br> **SARS-CoV-2 (n-coronavirus)** SARS-CoV-2 (n-coronavirus) là loại virus mới thuộc họ coronavirus, *được phát hiện* lần đầu vào năm 2019, chưa được xác định ở người trước đây.

Nó là một loại vi-rút *truyền nhiễm* bắt đầu từ **Vũ Hán** vào **tháng 12 năm 2019**. Sau này, nó được **WHO** tuyên bố là **đại dịch** do tốc độ lây lan cao trên toàn thế giới. Tính tới ngày 10 tháng 6 năm 2020, đại dịch này đã khiến hơn *500 nghìn* người chết trên toàn cầu.<br>

Đại dịch đang lan rộng trên toàn thế giới; điều quan trọng bây giờ là hiểu rõ hơn về sự lây lan này. Project này sẽ nỗ lực phân tích dữ liệu tích lũy của các trường hợp đã xác nhận, trường hợp tử vong và hồi phục theo thời gian.

## How to Install and Run the Project
1. Tải các tệp liên quan về kho lưu trữ của bạn (driver hoặc trên máy tính).

2. Bạn mở tệp notebook bằng Jupyter Notebook, Google Colab hoặc bất cứ môi trường nào để có thể chạy tệp notebook.

3. Cài đặt các thư viện cần thiết có trong bài:
* pandas
* numpy
* matplotlib
* pycountry_convert
* folium
* plotly.express
* plotly.graph_objs
* json
* plotly.offline
* seaborn

## Pipeline 

## Datasets

## How to Use the Project
**1. Giới thiệu dự án**

**2. Tải và cài đặt các thư viện theo yêu cầu**

**3. Tải Tập dữ liệu**

**4. Tìm hiểu dữ liệu**

**5. Phân tích toàn cầu**

* **Bài toán 1:** Tính số lượng tổng số trường hợp Covid, tổng số ca tử vong, tổng số ca phục hồi và số ca còn đang mắc Covid theo thời gian (đơn vị ngày).

* **Bài toán 2:** Hiển thị số lượng và log(10) của tổng số trường hợp Covid, tổng số ca tử vong, tổng số ca phục hồi và tổng số ca còn mắc covid theo thời gian (đơn vị ngày) trong 2 biểu đồ (một cho số lượng và một cho log(10)) bằng cách sử dụng biểu đồ đường.

* **Bài toán 3:** Hiển thị tổng số trường hợp Covid, tổng số ca tử vong, tổng số ca phục hồi và tổng số ca còn mắc covid theo thời gian (đơn vị ngày) ở 4 biểu đồ riêng biệt bằng cách sử dụng biểu đồ đường.

* **Bài toán 4:** Tính số lượng gia tăng hàng ngày về: tổng số ca mắc Covid, tổng số ca tử vong, tổng số ca phục hồi và tổng số ca còn mắc Covid theo thời gian (đơn vị ngày).

* **Bài toán 5:** Tính số lượng gia tăng hàng ngày về: tổng số ca mắc Covid, tổng số ca tử vong, tổng số ca phục hồi và tổng số ca còn mắc Covid theo thời gian (đơn vị ngày ở 4 biểu đồ riêng biệt).

* **Bài toán 6:** Tính phần trăm tỷ lệ tử vong toàn cầu và tỷ lệ hồi phục theo thời gian.

* **Bài toán 7:**

**7.1.** Hiển thị tỷ lệ tử vong theo thời gian (đơn vị ngày) bằng biểu đồ đường. Sử dụng đường gạch ngang để hiển thị tỷ lệ tử vong trung bình theo thời gian.

**7.2.** Hiển thị tỷ lệ hồi phục theo thời gian (đơn vị ngày) bằng biểu đồ đường. Sử dụng đường gạch ngang để hiển thị tỷ lệ tử vong trung bình theo thời gian.

**6. Phân tích châu lục**

* **Bài toán 8:** Thêm trường "continent" vào tập dữ liệu confirm_df, death_df và recorveries_df:

* **Bài toán 9:** Tạo data frame country_df với chỉ mục là trường "Country/Region".
Các cột thông tin này gồm:
* continent: Châu lục.
* Confirmed: Tổng số ca mắc.
* Deaths: Tổng số ca tử vong.
* Recoveries: Tổng số ca hồi phục.
* Active: Tổng số ca còn mắc Covid.
* Mortality Rate: Tỷ lệ tử vong tính theo phần trăm.

* **Bài toán 10:** Tạo data frame continents_df với chỉ mục là trường "continent".
Các cột thông tin này gồm: 
* Confirmed: Tổng số ca mắc.
* Deaths: Tổng số ca tử vong.
* Recoveries: Tổng số ca hồi phục.
* Active: Tổng số ca còn mắc Covid.
* Mortality Rate: Tỷ lệ tử vong tính theo phần trăm.

* **Bài toán 11:** Áp dụng hàm visual_covid_case để hiển thị trực quan hóa của 7 lục địa trong 7 biểu đồ đường riêng biệt. Thứ tự của các trực quan hóa được sắp xếp theo thứ tự giảm dần theo số ca mắc được xác nhận.

* **Bài toán 12:** Trực quan hóa ma trận hiệp phương sai cho continents_df.

* **Bài toán 13:** Xây dựng biểu đồ tròn để so sánh tỷ lệ số ca mắc được xác nhận, số ca tử vong, số ca phục hồi và số ca vẫn còn mắc của 7 châu lục.
* Mỗi trường (confirm, deaths, ...) nên được trình bày trong các biểu đồ tròn khác nhau.
* Bạn không được sử dụng đoạn code lặp lại ở đây, hãy thử sử dụng vòng lặp for.
* Mỗi châu lục nên được trình bày bằng các màu sắc khác nhau.

**7. Phân tích quốc gia**

* **Bài toán 14:** Xây dựng bản đồ folium để hiển thị số ca được xác nhận, số ca tử vong, số ca phục hồi và tỷ lệ tử vong của mỗi quốc gia dựa trên vị trí của các quốc gia. Bán kính của vòng tròn tỷ lệ thuận với số ca được xác nhận.

* **Bài toán 15:** Xây dựng bản đồ px (plotly.express) để hiển thị số ca còn mắc Covid của mỗi quốc gia trong log(10) dựa trên tên các quốc gia bằng cách sử dụng màu "quang phổ".

* **Bài toán 16:** Lọc 10 quốc gia hàng đầu dựa trên số ca được xác nhận.

* **Bài toán 17:** Trực qua hóa 10 quốc gia được xác nhận hàng đầu với số ca vẫn còn mắc Covid, phục hồi và tử vong bằng cách sử dụng biểu đồ thanh xếp chồng lên nhau.

**8. Phân tích nâng cao**

* **Bài toán 18:** Trả lời câu hỏi

* **Bài toán 19:** Trả lời câu hỏi

* **Bài toán 20:** Trả lời câu hỏi

* **Bài toán 21:** Trả lời câu hỏi

* **Bài toán 22:** Trả lời câu hỏi

## Reference source

## Contributors

## Contact Information
* Email: *phamcongsu95@gmail.com*

