'''
Bài12:Viếtchươngtrìnhtínhkhoảngcách:
x=(v2   -u2)/2a
Trongđó u: vậntốc ban đầu, v vậntốccuốicùng, a giatốc
Distance = (v*v – u*u)/(2*a)
*ý tưởng
b1: hiển thị lời chào
b2: nhập số u, v, a
b3: tính :
'''
print("\t-------------------CALCULATOR DISTANCE-------------------")
u = float(input("Enter the value u= "))
v = float(input("Enter the value v= "))
a = float(input("Enterthe value a= "))
distance = ((v * v - u * u) / (2 * a))
print(f"Distance: ", distance)