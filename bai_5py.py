def kiem_tra_chuoi_con(s1, s2):
   #Su dung toan tu in de kiem tra su xuat hien cua chuoi con
   if s2 in s1: #nếu chuỗi s2 có ở trong chuỗi s1
       print(s1.count(s2)) #thì đếm số lần xuất hiện chuỗi s2
   else: #nếu không thì in ra dòng bên dưới
       print(f'Chuoi "{s2}" khong xuat hien trong chuoi "{s1}"')

try:
    t = int(input('số lượng các bộ test t: '))
    if(t>0 and t<=100):  # nếu nhập đúng điều kiện sẽ thực hiện ca câu lệnh phía dưới
        for i in range(t):  # cho i chạy từ 0 đến t
            s1 = input("nhap chuoi 1: ")
            s2 = input("nhap chuoi 2: ")
            print(f"test {i + 1}: ", end=" ")
            kiem_tra_chuoi_con(s1, s2)


    else:#nếu nhập vào số nhỏ hơn 0 và lớn hơn 100 thì sẽ in đoạn dưới ra và kết thức chương trình
        print("t phải nhỏ hơn 100 và lớn hơn 0")
except: # nếu nhập vào t không phải là số thì sẽ in dòng phía dưới và kết thúc chương trình
    print("không hợp lệ")