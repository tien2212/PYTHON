try:
    t = int(input('số lượng các bộ test t: '))
    if(t>0 and t<=100):  # nếu nhập đúng điều kiện sẽ thực hiện ca câu lệnh phía dưới
        str = []  # khởi tạo 1 mãng trống
        list_out = [] #danh sách chứa ký tự và số lần xuất hiện
        str_out = "[" #chuỗi chứa kết quả đầu ra theo định dạng
        for i in range(t):  # cho i chạy từ 0 đến t
            str.append(input())  # thực hiện thêm lần lượt các bộ test vào mãng str
        for i in range(len(str)):  #cho i chạy từ 0 đến độ dài của mãng str
            word = [] #khởi tạo mãng word
            print(f"\nTest {i+1}:") #thực hiện in dòng test i+1: với i+1 là số thứ tự bộ test
            # print("[", end='')
            for e in str[i]: #chạy vòng lập for trong str[i]
                if e not in word: #nếu e không nằm trong word thì thêm e với số lượng count vào trong list_out
                    if e != ' ': #loại bỏ dấu cách
                        list_out.append(f' {e}:{str[i].count(e)},')
                        word.append(e)  # và thêm e vào word để khi chạy lại if nếu gặp giống nhau sẽ bỏ qua
            for i in list_out:
                str_out+=i #thêm từng phàn tử vào trong str_out
            print(str_out.rstrip(','),"]", end='') #xuất kết quả đầu ra với rstrip là xóa dấu ',' ở cuối chuỗi

    else:#nếu nhập vào số nhỏ hơn 0 và lớn hơn 100 thì sẽ in đoạn dưới ra và kết thức chương trình
        print("t phải nhỏ hơn 100 và lớn hơn 0")
except: # nếu nhập vào t không phải là số thì sẽ in dòng phía dưới và kết thúc chương trình
    print("không hợp lệ")