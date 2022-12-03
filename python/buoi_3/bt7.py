#Bài 7: Viết chương trình tính biểu thức: (2x + 3y)2 + 3/2. Cho x = 19; y = 5. 
'''
*ý tưởng
b1: hiển thị lời chào
b2: nhập số x và y
b3: tính :
'''
print("\t-------------------CALCULATOR-------------------")
x = 19
y = 5
ket_qua = float(pow((2 * x +3 * y),2 +3 / 2))
print(f"Kết quả: ", ket_qua)