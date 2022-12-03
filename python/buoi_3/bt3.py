'''
viết chương trình tính diện tích hình tam giác
b1:hien thị lời chào
b2: nhập độ dài và chiều cao
b3: tính diện tích
    s = (a * h) / 2
b4: hiển thị kết quả
'''
print("\t-------------------CALCULATOR THE AREA OF TRIANGLE-------------------")
base = float(input("Enter base of triangle:"))
height = float(input("Enter height of triangle"))
area = (base * height) / 2
print(f"({base} * {height}) / 2: {area}")