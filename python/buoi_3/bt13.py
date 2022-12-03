'''
Bài 13:Viếtchươngtrìnhtínhlãiđơngiản
SI = (P*T*R)/100.0
p-- principle amount: sốtiềngốc , T-- time , R-- rate of interest: Lãisuất
*ý tưởng
b1: hiển thị lời chào
b2: nhập số tiền gốc, thời gian, lãi xuất
b3: tính :
'''
print("\t-------------------CALCULATOR INTEREST-------------------")
p = float(input("Enter the principle amount= "))
t = float(input("Enter time= "))
r = float(input("Enter the rate of interest= "))
SI = float((p*t*r)/100)
print(f"Interest: ", SI)