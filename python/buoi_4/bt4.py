'''
Bài 4: Viết một chương trình máy tính đơn giản. Cho người dùng nhập vào 2 số, sau đó sẽ hỏi người dùng 
lựa chọn 1 trong 4 phép tính: +, -, *, / và in ra kết quả tương ứng với phép tính đó.
Gợi ý: 
• Nhập giá trị là một số nguyên vào biến a
• Nhập giá trị là một số nguyên vào biến b
• Nhập phép tính cần dùng vào biến chon
• Nếu nhập dấu 
• Tính tổng của hai số
• In kết quả tính tổng hai số ra màn hình giá trị tổng a + b
• Nếu nhập dấu 
• Tính hiệu của hai số
• …tương tự cho các trường hợp còn lại

'''
#b1 thuc hien loi chao
print("\t-----PROGRAM TO CHECK LEAP YEAR-----")
#b2 nhap gia tri a va b
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
operator = input("Chose an operator (+,-,*,/): ")
result = 0;
#b3 xu li
if operator == '+':
    print("You have selected addition")
    result = a + b
    print(f"Addition of {a} and {b} is: {result}")
elif operator == '-':
    print("You have selected subtraction")
    result = a - b
    print(f"Subtraction of {a} and {b} is: {result}")
elif operator == '*':
    print("You have selected multiplication")
    result = a * b
    print(f"Multiplication of {a} and {b} is: {result}")
elif operator == '/':
    print("You have selected division")
    result = a / b
    print(f"Division of {a} and {b} is: {result}")
else:
    print("Some thing wrong, please check your option")



