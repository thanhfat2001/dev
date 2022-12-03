'''
: Tính diện tích hình chữ nhật trong Python
Trong bài tập này chúng ta sẽ thực hiện chương trình tính diện tích hình chữ nhật bằng Python. Đây là một dạng bài tập khá phổ biến khi học Python nói chung và ngôn ngữ lập trình nói riêng.
Ở bài tập này chúng ta sẽ nhận đầu vào từ người dùng bằng cách sử dụng hàm input(), sau đó tính diện tích hình chữ nhật dựa vào dữ liệu người dùng đã nhập.
Công thức : diện tích = chiều dài * chiều rộng
*ý tưởng
b1: hiển thị lời chào
b2: nhập số chieu dai` va rong
b3: tính :
    + dien tich hinh chu nhat
'''
print("\t-------------------CALCULATOR RECTANGULAR AREA-------------------")
longs = float(input("Enter longs: "))
width = float(input("Enter width: "))
area = longs * width
print(f"RECTANGULAR AREA= ", (area))
