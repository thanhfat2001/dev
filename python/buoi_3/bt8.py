'''Bài 8: Viết chương trình tính biểu thức: (35x - 5y) * 4z + 2531.
Tươngtựnhư ở phầntrên, chúng ta cũngsẽsửdụng hàminput() đểlấydữliệutừbànphím
*ý tưởng
b1: hiển thị lời chào
b2: nhập số x , y, z
b3: tính :

'''
print("\t-------------------CALCULATOR-------------------")
x = float(input("Enter the value x= "))
y = float(input("Enter the value y= "))
z = float(input("Enter the value z= "))
ket_qua = float((35 * x - 5 * y) * 4 * z + 2531)
print(f"Result: ", ket_qua)