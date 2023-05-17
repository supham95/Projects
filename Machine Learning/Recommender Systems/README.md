# Movie Recommendation Project

## Project Description
Sự phát triển nhanh chóng của việc thu thập dữ liệu đã dẫn đến một kỷ nguyên thông tin mới. Dữ liệu đang được sử dụng nhằm tạo ra các hệ thống giúp con người có thể đạt được nhiều mục tiêu một cách dễ dàng hơn. Trong phim ảnh, một Hệ Thống Đề Xuất ***`(recommender system)`*** có thể giúp con người nhanh chóng tiếp cận những bộ phim mà họ thích, giảm thời gian tìm kiếm và nhanh chóng tiếp cận đến người dùng. Hệ thống Đề xuất là một loại **hệ thống lọc thông tin** cải thiện chất lượng kết quả tìm kiếm và cung cấp các mục phù hợp hơn với mục tìm kiếm hoặc được xác định với lịch sử tìm kiếm của người dùng.

Project này sẽ xây dựng các loại Hệ Thống Đề Xuất khác nhau cho người dùng:

1. Dựa vào đánh giá của người dùng đến từng bộ phim ***`(demographic filtering)`***, từ đó có thể đề xuất những bộ phim nổi trội, đang được người dùng đánh giá tốt và bắt trend. 

2. Dựa trên nội dung phim ***`(content-based filtering)`***, từ đó có thể đề xuất những bộ phim tương quan với bộ phim mà người dùng đang xem hoặc chú ý đến. 

3. Dựa vào lịch sử đánh giá của người dùng về các bộ phim thông qua phương pháp Lọc Cộng Tác ***`(collaborative filtering)`***, cụ thể hơn sẽ sử dụng một phương pháp khác phục một số nhược điểm của Lọc Cộng Tác là Matrix Factorization.

## How to Install and Run the Project
1. Tải các tệp từ phần Tài nguyên về kho lưu trữ của bạn (driver hoặc trên máy tính).

2. Bạn mở tệp notebook bằng Jupyter Notebook, Google Colab hoặc bất cứ môi trường nào để có thể chạy tệp notebook.

3. Cài đặt các thư viện cần thiết có trong bài:
* pandas
* numpy
* matplotlib
* seaborn
* surprise
* sklearn

## Pipeline 

1. Đọc dữ liệu.

2. Xây dựng Hệ Thống Đề Xuất bằng phương pháp Demographic Filtering.

3. Xây dựng Hệ Thống Đề Xuất bằng phương pháp Content Based Filtering.
* Xây dựng bằng tổng quan của phim.
* Xây dựng bằng thông tin của phim bao gồm: đạo diễn, diễn viên chính, keywords, thể loại phim.

4. Xây dựng Hệ Thống Đề Xuất bằng phương pháp Collaborative Filtering bằng SVD.

## Datasets

**credits** bao gồm các đặc trưng sau:

* **movie_id**: id của phim
* **cast**: tên của các diễn viên chính và phụ.
* **crew**: tên của các nhân viên trong quá trình sản xuất phim (đạo diễn, editor, người soạn nhạc, v.v.)

**movies** bao gồm các đặc trưng sau:

* **budget**: kinh phí thực hiện bộ phim.
* **genre**: các thể loại của phim.
* **homepage**: liên kết đến trang chủ của bộ phim.
* **id**: thông tin về movie_id như trong tập dữ liệu tmdb_5000_credits.
* **keywords**: các từ khóa hoặc thẻ liên quan đến bộ phim.
* **original_language**: ngôn ngữ trong bộ phim sử dụng.
* **original_title**: tên phim trước khi dịch hoặc chuyển thể.
* **overview**: mô tả ngắn gọn về bộ phim.
* **popularity**: số lượng chỉ định mức độ phổ biến của bộ phim.
* **production_companies**: nhà sản xuất của bộ phim.
* **production_countries**: quốc gia sản xuất của bộ phim.
* **release_date**: ngày mà nó được phát hành.
* **revenue**: doanh thu trên toàn thế giới do bộ phim tạo ra.
* **runtime**: thời gian  của phim tính bằng phút.
* **status**: Đã phát hành hoặc còn là tin đồn.
* **tagline**: khẩu hiệu của phim.
* **title**: tên phim.
* **vote_average**: đánh giá trung bình mà bộ phim nhận được.
* **vote_count**: số lượng đánh giá.

## How to Use the Project
**Task 1.** Đọc dữ liệu creadits và movies và kết hợp 2 dữ liệu thành một dataframe

**Task 2.** Xây dựng hàm tính weighted_rating
* Tính giá trị C.
* Tính giá trị m bằng 90% số lượng đánh giá của toàn bộ dữ liệu.
* Xây dựng hàm tính weighted_rating.

**Task 3.** Tính điểm cho từng bộ phim từ hàm weighted_ratings và đề xuất phim
* Lọc những bộ phim có số lượng đánh giá ít nhất bằng m.
* Tính điểm cho từng bộ phim bằng hàm weighted_rating.
* Đề xuất 10 bộ phim dựa vào phương pháp đề xuất Demographic Filtering.

**Task 4.** Trực quan biểu đồ trực quan 10 bộ phim phổ biến nhất hiện nay bằng chỉ số popularity
* Sử dụng thư viện Matlotlib.

**Task 5.** Tính IF-IDF cho toàn bộ overview

**Task 6.** Tính ma trận tương tự cho overview từ TF-IDF

**Task 7.** Xây dựng hàm để đề xuất phim dựa vào tổng quan của phim
* Tạo một pandas Series với value là index của dữ liệu bộ phim, index là title của bộ phim.
* Lấy index của bộ phim thông qua title.
* Lấy danh sách giá trị tương đồng của bộ phim cụ thể theo index so với tất cả các bộ phim. Chuyển nó thành một danh sách các bộ giá trị trong đó phần tử đầu tiên là index và phần tử thứ hai là giá trị tương tự.
* Sắp xếp danh sách trên theo giá trị tương tự giảm dần.
* Lấy ra 10 phần tử đầu từ danh sách trên (10 phần tử này là 10 bộ phim có mức độ tương tự so với phim hiện tại mà ta muốn khuyến nghị). Chú ý là loại bỏ phần tử đầu tiên và bắt đầu lấy từ phẩn tử thứ 2 vì phần tử đầu tiên là chính bộ phim đó. Do là chính bộ phim đó nên giá trị tương tự rất lớn.
* Trả về tiêu đề theo index có trong danh sách 10 bộ phim mà ta muốn khuyến nghị.
* Đưa ra khuyến nghị cho phim 'The Dark Knight Rises' và 'The Avengers'.

**Task 8.** Lấy ra tên tác giả từ cột crew và lưu vào cột director

**Task 9.** Lấy ra 3 diễn viên đầu tiên từ cột cast và lưu vào chính cột cast. Làm điều tương tự với keywords và genres

**Task 10.** Điều chỉnh dữ liệu phù hợp với đầu vào của thuật toán

**Task 11.** Kết hợp dữ liệu của từng giá trị trong keywords, cast, director, genres thành một chuỗi và lưu vào cột movie_info

**Task 12.** Tính CountVectorizer cho từng movie_info

**Task 13.** Tính ma trận tương tự cho movie_info từ CountVectorizer.
* Sử dụng hàm get_recommendations()với ma trận tương tự mới: cosine_sim2 để đưa ra những bộ phim đề xuất khi người dùng xem phim 'The Dark Knight Rises' và 'The Godfather'.

**Task 14.** Đọc dữ liệu đánh giá phim của người dùng.

**Task 15.** Xử lý dữ liệu đầu vào phù hợp với SVD của surprise

**Task 16.** Sử dụng K-Fold để huấn luyện và đánh giá mô hình

## Reference source

## Contributors

## Contact Information
* Email: *phamcongsu95@gmail.com*
