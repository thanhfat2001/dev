'''
Bài 5: Cho nhập vào 2 số thực a và b. Hãy tính tổng, hiệu tích thương giá trị 2 số hạng đó.
Gợi ý:
Sử dụng hàm : str() , int(), float() để ép kiểu dữ liệu.
Sử dụng hàm input() để nhập dữ liệu từ bàn phím, để chúng ta có thể nhận được các giá trị của cả hai số từ người dùng. Chương trình sau đó sẽ thực hiện tính tổng, hiệu , tích , thương và hiển thị nó.
* ý tưởng 
b1: hiển thị lời chào
b2: nhập số a và b
b3: tính :
    + cong
    + tru
    + nhan
    +chia
'''
print("\t-------------------CALCULATOR OF THE NUMBER-------------------")

a = float(input("Enter number a = "))
b = float(input("Enter number b = "))
add = a + b
sub = a - b
mul = a * b
div = a / b
print(f"{add} \t, {sub} \t, {mul} \t, {div}")