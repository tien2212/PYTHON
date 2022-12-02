try:
    t = int(input('số lượng các bộ test t: '))
    if(t>0 or t<=100):  # nếu nhập đúng điều kiện sẽ thực hiện ca câu lệnh phía dưới
        str = []  # khởi tạo 1 mãng trống
        for i in range(t):  # cho i chạy từ 0 đến t
            str.append(input())  # thực hiện thêm lần lượt các bộ test vào mãng str
        for i in range(len(str)):  # cho i chạy từ 0 đến độ dài của mãng str
            print(f"Test {i + 1}:")  # thực hiện in dòng test i+1: với i+1 là số thứ tự bộ test
            print(str[i].title())  # in lần lược các chuỗi trong mãng với title là viết hoa các chữ cái đầu

    else:#nếu nhập vào số nhỏ hơn 0 và lớn hơn 100 thì sẽ in đoạn dưới ra và kết thức chương trình
        print("t phải nhỏ hơn 100 và lớn hơn 0")
except: # nếu nhập vào t không phải là số thì sẽ in dòng phía dưới và kết thúc chương trình
    print("không hợp lệ")


