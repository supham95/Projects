# ĐỒ ÁN CUỐI KHÓA KHOA HỌC DỮ LIỆU - DSP305
# DỰ ĐOÁN LƯỢNG KHÁCH DU LỊCH

## Giới thiệu
* Đồ án được lấy từ một cuộc thi trên kaggle, yêu cầu xây dựng mô hình dự đoán lượng khách du lịch để cung cấp thông tin chính xác về nhu cầu du lịch trong tương lai của Nhật Bản,
giúp các doanh nghiệp và cơ quan liên quan đưa ra các quyết định kinh doanh và phát triển phù hợp, góp phần thúc đẩy sự phát triển của ngành du lịch.
* [Chi tiết cuộc thi](https://www.kaggle.com/competitions/prediction-of-tourist-arrivals/overview)

## Chỉ số đánh giá
* Sai số bình phương trung bình gốc – RMSE (theo quy định của cuộc thi trên kaggle)

## Điều kiện tiên quyết
*Trước khi tiếp tục, hãy đảm bảo các yêu cầu sau:*
* Ngôn ngữ lập trình: Python
* Library/Package/Framework:
  + Xử lý dữ liệu: pandas, numpy, datetime, jpholiday
  + Thống kê và phân tích dữ liệu: numpy, sklearn
  + Học máy: sklearn, keras, optuna, lightgbm, xgboost, catboost
  + Vẽ đồ thị: matplotlib, seaborn

## Thuật toán:
* Áp dụng thuật toán học máy Gradient Boosting, 3 framework:
  + [LightGBM](https://lightgbm.readthedocs.io/en/stable/)
  + [XGBoost](https://xgboost.readthedocs.io/en/stable/)
  + [CatBoost](https://catboost.ai/)

## Cấu trúc thư mục
* Data: Lưu trữ dữ liệu thô
* Final_project.ipynb: mã nguồn (source code)
* Slide.pdf: Báo cáo đồ án (file PDF)
* README.md

## Cách sử dụng
1. Cài đặt các thư viện cần thiết
2. Chạy file Final_project.ipynb
3. Xem Slide.pptx để biết thêm chi tiết về phân tích dữ liệu và xây dựng mô hình

## Tài liệu tham khảo
* LightGBM Website. [Welcome to LightGBM’s documentation!](https://lightgbm.readthedocs.io/en/stable/)
* XGBoost Website. [XGBoost Documentation](https://xgboost.readthedocs.io/en/stable/)
* CatBoost Website. [CatBoost Documentation](https://catboost.ai/en/docs/)
* KENTAK0928 (2023). [Prediction of Tourist Arrivals](https://www.kaggle.com/competitions/prediction-of-tourist-arrivals/overview)
* Aarshay Jain (2023). [Mastering XGBoost Parameter Tuning: A Complete Guide with Python Codes](https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/#XGBoost_Parameters)
* MJ Bahmani (2023). [Understanding LightGBM Parameters](https://neptune.ai/blog/lightgbm-parameters-guide)
* Mario Filho (2023). [CatBoost Hyperparameter Tuning Guide with Optuna](https://forecastegy.com/posts/catboost-hyperparameter-tuning-guide-with-optuna/)
* Pham Minh Hoang (2020). [Ensemble learning và các biến thể](https://viblo.asia/p/ensemble-learning-va-cac-bien-the-p1-WAyK80AkKxX)
* Brain John (2023). [When to Choose CatBoost Over XGBoost or LightGBM](https://neptune.ai/blog/when-to-choose-catboost-over-xgboost-or-lightgbm)

## Liên hệ
* *Pham Cong Su*
* *Email: supcfx16803@funix.edu.vn / phamcongsu95@gmail.com*
