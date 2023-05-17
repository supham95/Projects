# European Football Data Retrieval And Analysis Project

## Project Description
Bạn nhận được cơ sở dữ liệu bóng đá châu Âu có hơn 25.000 trận đấu và hơn 10.000 cầu thủ cho các mùa bóng đá chuyên nghiệp châu Âu từ 2008 đến 2016. Bạn cần phải xem cơ sở dữ liệu này và thực hiện phân tích, bao gồm một số bước khám phá dữ liệu, thống kê cơ bản và sau đó trực quan hoá kết quả. Để hoàn thành tất cả các bước, bạn cần truy vấn dữ liệu trong cơ sở dữ liệu bằng cách sử dụng câu lệnh SQL. 

Thông qua dự án này, ban có thể thực hành viết lệnh SQL để lấy dữ liệu về và trích xuất nó:
* Kết nối với cơ sở dữ liệu sqlite bằng lập trình Python
* Viết câu lệnh SQL: Select, group by, order by
* Viết câu lệnh SQL nâng cao: Union
* Viết truy vấn con

## How to Install and Run the Project
1. Tải dữ liệu Soccer Database và Jupyter Notebook

2. Mở Jupyter Notebook

3. Import Python package: sqlite, numpy, pandas

4. Kết nối với sqlite database để truy vấn dữ liệu

## Pipeline 

## Datasets

## How to Use the Project
**Câu hỏi 1:** Kết nối cơ sở dữ liệu

* Sử dụng Python để kết nối với cơ sở dữ liệu SQLite
* Lấy thông tin của tất cả các bảng

**Câu hỏi 2:** Liệt kê các quốc gia có trong bảng "Country"

**Câu hỏi 3:** Liệt kê các giải đấu trong bảng "League"

**Câu hỏi 4:** Liệt kê các giải đấu và thông tin quốc gia của từng giải

**Câu hỏi 5:** Liệt kê các trận đấu trong bảng  “Match”

**Câu hỏi 6:** Liệt kê các trận đấu và thông tin về leage và country tương ứng

**Câu hỏi 7:** Liệt kê số lượng trận đấu của mỗi giải đấu bao gồm cả tên giải đấu, sắp xếp theo thứ tự giảm dần số trận đấu

**Câu hỏi 8:** Liệt kê tổng số bàn thắng của đội nhà và đội khách trong mỗi giải đấu

**Câu hỏi 9:** Liệt kê thông tin các đội từ bảng “Team”

**Câu hỏi 10:** Liệt kê 20 đội với số bàn thắng sân nhà cao nhất

**Câu hỏi 11:** Liệt kê 20 đội có số bàn thắng trên sân khách cao nhất

**Câu hỏi 12:** Liệt kê tên các đội bóng và tổng số bàn thắng mỗi đội, sắp xếp theo số lượng giảm dần

**Câu hỏi 13:** Liệt kê tên các đội bóng (long name) và tổng số trận đấu đội đó tham gia, sắp xếp theo thứ tự giảm dần

**Câu hỏi 14:** Liệt kê số trận thắng, thua và hòa của mỗi đội.

* Nếu một đội có số lượng bàn thắng trên sân nhà > số lượng bàn thắng trên sân khách của chính đội đó, thì đội đó sẽ "thắng" trong trận đấu này
* Nếu một đội có số lượng bàn thắng trên sân nhà < số lượng bàn thắng trên sân khách của chính đội đó, thì đội đó sẽ "thua" trong trận đấu này
* Nếu một đội có số lượng bàn thắng trên sân nhà = số lượng bàn thắng trên sân khách của chính đội đó, thì đội đó sẽ "hòa" trong trận đấu này
* Sử dụng câu lệnh "Case When"

**Câu hỏi 15:** Liệt kê 10 đội có số trận thắng nhiều nhất

**Câu hỏi 16:** Liệt kê tỉ lệ phần trăm về số trận của mỗi giải trên tổng tất cả các trận

**Câu hỏi 17:** Liệt kê tỉ lệ phần trăm về số bàn ghi được của từng giải so với tổng số bàn của tất cả các trận

**Câu hỏi 18:** Liệt kê tổng số bàn ghi được của từng giải đấu theo từng mùa giải

**Câu hỏi 19:** Liệt kê thông tin cầu thủ:

* Cân nặng: chuyển đổi sang đơn vị kg
* Chiều cao: chuyển đổi chiều cao sang đơn vị mét
* BMI: tính toán BMI cơ sở trên cân nặng và chiều cao.
* Tuổi của cầu thủ

**Câu hỏi 20:** Liệt kê cầu thủ lớn tuổi nhất

**Câu hỏi 21:** Liệt kê cầu thủ có số trận đấu nhiều nhất

**Câu hỏi 22:** Liệt kê các cầu thủ có tổng số điểm đánh giá lớn hơn 80

## Reference source

## Contributors

## Contact Information
* Email: *phamcongsu95@gmail.com*

