def thay_the(s1, s2, s3):
    print(s1.replace(s2, s3))

try:
    t = int(input('số lượng các bộ test t: '))
    if(t>0 and t<=100):  # nếu nhập đúng điều kiện sẽ thực hiện ca câu lệnh phía dưới
        for i in range(t):  # cho i chạy từ 0 đến t
            s1 = input("nhap chuoi: ")
            s2 = input("nhap chuoi thay the cu: ")
            s3 = input("nhap chuoi thay the mơi: ")
            print(f"test {i + 1}:", end="\n")
            thay_the(s1, s2, s3)

    else:#nếu nhập vào số nhỏ hơn 0 và lớn hơn 100 thì sẽ in đoạn dưới ra và kết thức chương trình
        print("t phải nhỏ hơn 100 và lớn hơn 0")
except: # nếu nhập vào t không phải là số thì sẽ in dòng phía dưới và kết thúc chương trình
    print("không hợp lệ")