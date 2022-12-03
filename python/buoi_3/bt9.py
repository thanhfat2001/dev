'''Bài9: Tính Speed
Tươngtựnhư ở phầntrên, chúng ta cũngsẽsửdụng hàminput() đểlấydữliệutừbànphím.
Gợi ý:
Cho nhậpvàocácgiátrịsốthựcvàgánvàocácbiến: u, v, a
Côngthức: S = (v * v – u * u) / (2 * a) 
Xuấtrakếtquả S
*ý tưởng
b1: hiển thị lời chào
b2: nhập số u , v, a
b3: tính :
'''
print("\t-------------------CALCULATOR OF SPEED-------------------")
u = float(input("Enter the value u= "))
v = float(input("Enter the value v= "))
a = float(input("Enter the value a= "))
speed = float((v * v - u * u) / (2 * a) )
print(f"Result: ", speed)