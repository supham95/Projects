import pandas as pd
import re

# TASK 1
# Vòng lặp: Khi file không tìm thấy để đọc sẽ quay lại bước nhập tên file
while True:
    try:
        # Để user nhập tên file cần đọc
        file_name = input('Enter a class file to grade (i.e. class1 for class1.txt):')
        # Mở file và đọc
        rf = pd.read_csv(file_name + '.txt', sep=' ', header=None)
        # Nếu file mở đọc thành công sẽ in ra 'Successfully opened...'
        print('Successfully opened {}'.format(file_name+ '.txt'))
        # Dùng break thoát khỏi vòng lặp while khi đã mở và đọc được file
        break
    # Trường hợp file không tồn tại, in ra 'File cannot be found' và cho user nhập lại tên file
    except FileNotFoundError:
        print('File cannot be found.')

# TASK 2
print('**** ANALYZING ****')
# Tách dữ liệu ID sinh viên và câu trả lời ra thành 2 cột từ rf, đặt tên cho DataFrame mới là df_answer
df_answer = rf[0].str.split(',', expand=True, n=1)
# Đặt tên cho 2 cột trong df_answer là ID: lưu thông tin ID sinh viên, và answer: lưu câu trả lời
df_answer.columns = ['ID', 'answer']
# Số dòng hợp lệ
valid_num = 0
# Số dòng không hợp lệ
invalid_num = 0
# Tạo DataFrame các dòng hợp lệ
df_valid = df_answer
for index, row in df_answer.iterrows():
    # Sử dụng split để tách dữ liệu answer theo dấu ','
    std = row['answer'].split(',')
    # Dùng findall trong regex để lấy dữ liệu số ID của sinh viên chứa ký tự “N” theo sau là 8 ký tự số
    f_data = re.findall('[N]{1}\d{8}', row['ID'])
    # Nếu dòng không chứa đủ 25 câu trả lời:
    if len(std) != 25:
        print('Invalid line of data: does not contain exactly 25 values:\n{}'.format(std))
        invalid_num += 1  # Số dòng không hợp lệ tăng thêm 1
        df_valid = df_valid.drop(index)
    # Nếu dòng có số ID sinh viên không hợp lệ:
    elif len(f_data) < 1:
        print('Invalid line of data: N# is invalid:\n{}'.format(std))
        invalid_num += 1  # Số dòng không hợp lệ tăng thêm 1
        df_valid = df_valid.drop(index)
    else:
        valid_num += 1  # Số dòng hợp lệ tăng thêm 1
# Nếu tất cả các dòng đều hợp lệ, in ra No errors found!
if invalid_num == 0:
    print('No errors found!')
# In ra số dòng hợp lệ và không hợp lệ:
print('**** REPORT ****')
print('Total valid lines of data: {}'.format(valid_num))
print('Total invalid lines of data: {}'.format(invalid_num))

# TASK 3
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
# Tách chuỗi answer_key theo dấu ',' và chuyển sang list
ans = answer_key.split(',')
# Tạo DataFrame rỗng để chứa điểm
df_score = pd.DataFrame()
# Tạo dict rỗng để add các câu trả lời bị bỏ qua
skip_dct = dict()
# Tạo dict rỗng để add các câu trả lời sai
wrong_dct = dict()
# Xét từng sinh viên trong df_valid
for index, row in df_valid.iterrows():
    # Sử dụng split để tách dữ liệu theo dấu ','
    line = row['answer'].split(',')
    # Tạo biến điểm số
    score = 0
    # Tạo vòng lặp for chạy từ 0 tới 24, vì có 25 câu trả lời
    for i in range(25):
        # So sánh từng câu trả lời với đáp án, nếu đúng + 4 vào score, nếu sai -1 vào score, bỏ trống thì được 0 điểm
        if line[i] == ans[i]:
            score += 4
        elif len(line[i]) == 0:
            # Thêm câu trả lời bỏ trống vào dict skip_dct, nếu câu này đã có trong dict thì số lượng sai + 1
            skip_dct[i+1] = skip_dct.get(i+1, 0) + 1
        elif line[i] != ans[i]:
            score -= 1
            # Thêm câu trả lời sai vào dict wrong_dct, nếu câu này đã có trong dict thì số lượng sai + 1
            wrong_dct[i+1] = wrong_dct.get(i+1, 0) + 1
    if score < 0:
        score = 0  # Vì không có điểm âm, điểm thấp nhất là 0
    # add điểm vào df_score
    dff = pd.DataFrame({'ID': row['ID'], 'score': score}, index=[index])
    df_score = df_score.append(dff)
print('Total student of high scores: {}'.format(df_score[df_score['score']>80]['score'].count()))
# Điểm trung bình
print('Mean (average) score: {}'.format(df_score['score'].mean()))
# Điểm cao nhất
print('Highest score: {}'.format(df_score['score'].max()))
# Điểm thấp nhất
print('Lowest score: {}'.format(df_score['score'].min()))
# Miền giá trị của điểm
print('Range of scores: {}'.format(df_score['score'].max() - df_score['score'].min()))
# Giá trị trung vị
print('Median score: {}'.format(df_score['score'].median()))

# Tạo hàm thống kê số câu trả lời bỏ qua nhiều nhất và số câu trả lời sai nhiều nhất
# input: dictionary chứa dữ liệu câu trả lời bỏ qua/sai, số lượng sinh viên (có câu trả lời hợp lệ)
# output: số thứ tự câu hỏi - số lượng học sinh bỏ qua/sai -  tỉ lệ bị bỏ qua/sai
def score_analysis(dctn, valid_number):
    max_value = max(list(dctn.values()))
    for key, val in dctn.items():
        if val == max_value:
            rate = round((val/valid_number), 3)
            print(key,' - ',val,' - ',rate, end=', ')

# Trả về các câu hỏi bị học sinh bỏ qua nhiều nhất:
print('Question that most people skip: ',end='')
score_analysis(skip_dct, valid_num)
# Trả về các câu hỏi bị sai nhiều nhất:
print('\nQuestion that most people answer incorrectly: ',end='')
score_analysis(wrong_dct, valid_num)

# TASK 4
# Lưu trữ kết quả
df_score.to_csv(file_name + '_grades.txt', index=None, header=False)
print('\nFolder {} has been created'.format(file_name + '_grades.txt'))