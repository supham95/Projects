import re
import statistics
# TASK 1
# Vòng lặp: Khi file không tìm thấy để đọc sẽ quay lại bước nhập tên file
while True:
    try:
        # Để user nhập tên file cần đọc
        file_name = input('Enter a class file to grade (i.e. class1 for class1.txt):')
        # Mở file và đọc
        with open(file_name + '.txt','r') as rf:
            # Đọc toàn bộ file, hàm readlines() trả về một list tương ứng mỗi dòng dữ liệu là 1 phần tử của list
            result = rf.readlines()
            # Nếu file mở đọc thành công sẽ in ra 'Successfully opened...'
            print('Successfully opened {}'.format(file_name + '.txt'))
            # Dùng break thoát khỏi vòng lặp while khi đã mở và đọc được file
            break
    # Trường hợp file không tồn tại, in ra 'File cannot be found' và cho user nhập lại tên file
    except FileNotFoundError:
        print('File cannot be found.')

# TASK 2
print('**** ANALYZING ****')
valid_num = 0  # Số dòng hợp lệ
invalid_num = 0  # Số dòng không hợp lệ
valid_lst = []  # Tạo list các dòng hợp lệ
# Xét từng list trong result
for lst in result:
    # Sử dụng strip để bỏ khoảng trống xuống dòng ở cuối lst, dùng split để tách dữ liệu theo dấu ','
    std = (lst.strip()).split(',')
    # Dùng findall trong regex để lấy dữ liệu số ID của sinh viên chứa ký tự “N” theo sau là 8 ký tự số
    f_data = re.findall('[N]{1}\d{8}', lst)
    # Nếu dòng không chứa đủ 26 ký tự:
    if len(std) != 26:
        print('Invalid line of data: does not contain exactly 26 values:\n{}'.format(std))
        invalid_num += 1  # Số dòng không hợp lệ tăng thêm 1
    # Nếu dòng có số ID sinh viên không hợp lệ:
    elif len(f_data) < 1:
        print('Invalid line of data: N# is invalid:\n{}'.format(std))
        invalid_num += 1  # Số dòng không hợp lệ tăng thêm 1
    else:
        valid_num += 1  # Số dòng hợp lệ tăng thêm 1
        # Thêm dòng hợp lệ vào valid_lst
        valid_lst.append(lst)
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
# Tạo dict rỗng để add key là ID sinh viên, value là điểm số
dct_student = dict()
# Tạo dict rỗng để add các câu trả lời bị bỏ qua
skip_dct = dict()
# Tạo dict rỗng để add các câu trả lời sai
wrong_dct = dict()
# Xét từng list trong result
for lst in valid_lst:
    # Sử dụng strip để bỏ khoảng trống xuống dòng ở cuối lst, dùng split để tách dữ liệu theo dấu ','
    line = (lst.strip()).split(',')
    # Tạo biến điểm số
    score = 0
    # Tạo vòng lặp for chạy từ 0 tới 24, vì có 25 câu trả lời
    for i in range(25):
        # So sánh từng câu trả lời với đáp án, nếu đúng + 4 vào score, nếu sai -1 vào score, bỏ trống thì được 0 điểm
        # Vì giá trị đầu tiền của line là ID sinh viên, nên câu trả lời sẽ từ line[1]
        if line[i + 1] == ans[i]:
            score += 4
        elif len(line[i + 1]) == 0:
            # Thêm câu trả lời bỏ trống vào dict skip_dct, nếu câu này đã có trong dict thì số lượng sai + 1
            skip_dct[i + 1] = skip_dct.get(i + 1, 0) + 1
        elif line[i + 1] != ans[i]:
            score -= 1
            # Thêm câu trả lời sai vào dict wrong_dct, nếu câu này đã có trong dict thì số lượng sai + 1
            wrong_dct[i + 1] = wrong_dct.get(i + 1, 0) + 1
    if score < 0:
        score = 0  # Vì không có điểm âm, điểm thấp nhất là 0
    # add điểm vào dct
    dct_student[line[0]] = score
# Lấy ra list điểm của các sinh viên từ dict
value = list(dct_student.values())
# Đếm số lượng học sinh đạt điểm cao (>80)
high_score = 0
for x in value:
    if x > 80: high_score += 1
print('Total student of high scores: {}'.format(high_score))
# Điểm trung bình
print('Mean (average) score: {}'.format(sum(value)/len(value)))
# Điểm cao nhất
print('Highest score: {}'.format(max(value)))
# Điểm thấp nhất
print('Lowest score: {}'.format(min(value)))
# Miền giá trị của điểm
print('Range of scores: {}'.format(max(value) - min(value)))
# Giá trị trung vị
print('Median score: {}'.format(statistics.median(value)))

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
list_student = []
for k,v in dct_student.items():
    list_student.append(str(k) + ',' + str(v))
name = file_name + '_grades.txt'
with open(name,'w') as wf:
    for text in list_student:
        wf.write(text + '\n')
print('\nFolder {} has been created'.format(name))