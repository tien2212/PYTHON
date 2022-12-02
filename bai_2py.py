def demNguyenAm_PhuAm(str): #tạo hàm đếm nguyên âm và phụ âm
    nguyenAm = 0 #gán nguyên âm = 0
    phuAm = 0 # gán phụ âm = 0
    for i in str: #chạy vòng lập for với từng phần trong str
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
                i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'): #điều kiện để xác định đó là nguyên âm
            nguyenAm = nguyenAm + 1 #nếu điều kiện đúng thì nguyên âm được cộng thêm 1
        elif(i != ' '): #và ngược lại nếu k phải ' ' thì phụ âm công thêm 1
            phuAm = phuAm + 1
    print("Số nguyên âm: ",nguyenAm) #xuất số nguyên âm
    print("Số phụ âm: ",phuAm)    #xuất số phụ âm

try:
    t = int(input('số lượng các bộ test t: '))
    if(t>0 and t<=100):  # nếu nhập đúng điều kiện sẽ thực hiện ca câu lệnh phía dưới
        str = []  # khởi tạo 1 mãng trống
        for i in range(t):  # cho i chạy từ 0 đến t
            str.append(input())  # thực hiện thêm lần lượt các bộ test vào mãng str
        for i in range(len(str)):  #cho i chạy từ 0 đến độ dài của mãng str
            print(f"Test {i + 1}:") #thực hiện in dòng test i+1: với i+1 là số thứ tự bộ test
            demNguyenAm_PhuAm(str[i])

    else:#nếu nhập vào số nhỏ hơn 0 và lớn hơn 100 thì sẽ in đoạn dưới ra và kết thức chương trình
        print("t phải nhỏ hơn 100 và lớn hơn 0")
except: # nếu nhập vào t không phải là số thì sẽ in dòng phía dưới và kết thúc chương trình
    print("không hợp lệ")

