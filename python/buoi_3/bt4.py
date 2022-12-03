'''Bài 4: Cho hằng số: pi = 3.14. Bán kính là một số thực sinh viên có thể tự cho. Viết chương trình tính chu vi và diện tích hình tròn. 
Gợi ý:
•	Cho 1 biến là bán kính, 1 biến là hằng số pi
•	Sau đó, gán công thức vào biến chu vi, diện tích
•	Dùng lệnh print() để in kết quả ra màn hình
Công thức: 
	Diện tích:  Math.PI * (radius * radius)
	Chu vi: Math.PI * 2*radius
* ý tưởng 
b1: hiển thị lời chào
b2: nhập bán kính, PI (là một hằng số)
b3: tính :
    + chu vi
    +diện tích
'''
import math
print("\t-------------------CALCULATOR THE CIRCLE-------------------")
radius = float(input("Enter the radius: "))
PI = math.pi #sử dụng thư viện math dể gọi giá trị biến pi và gán cho pi
#tính chu vi
circum = PI * 2 * radius
#diện tích
area = PI * (radius * radius)
#hiển thị kết quả
print(f"Circum: {circum} , \t Area: {area}")