def inds(str): #taoh hàm in danh sách
    word = str.split() #chuyển mãng str về dạng split
    for i in word: #chạy vòng lập for với word đã chuyển dạng split
        print(i, end=' ')#in ra kết quả


try:
    t = int(input('số lượng các bộ test t: '))
    if(t>0 and t<=100):  # nếu nhập đúng điều kiện sẽ thực hiện ca câu lệnh phía dưới
        str = []  # khởi tạo 1 mãng trống
        for i in range(t):  # cho i chạy từ 0 đến t
            str.append(input())  # thực hiện thêm lần lượt các bộ test vào mãng str
        for i in range(len(str)):  #cho i chạy từ 0 đến độ dài của mãng str
            print(f"\nTest {i+1}:",end='\n') #thực hiện in dòng test i+1: với i+1 là số thứ tự bộ test
            inds(str[i]) #in ra kết quả của bộ test khi gắn vào hàm in danh sách

    else:  # nếu nhập vào số nhỏ hơn 0 và lớn hơn 100 thì sẽ in đoạn dưới ra và kết thức chương trình
        print("t phải nhỏ hơn 100 và lớn hơn 0")
except:  # nếu nhập vào t không phải là số thì sẽ in dòng phía dưới và kết thúc chương trình
    print("không hợp lệ")

