'''Bài11:Giảiphươngtrìnhbậc 2: ax2 + bx + c = 0
Tínhnghiệmcủaphươngtrình: 
x=(-b±√(b^2-4ac))/2a
x1 = (- b + sqrt(b*b-4*a*c))/(2*a);
x2 = (- b - sqrt(b*b-4*a*c))/(2*a);
*ý tưởng
b1: hiển thị lời chào
b2: nhập số n
b3: tính :
'''
import math

print("\t-------------------CALCULATOR-------------------")
a = float(input("Enter the value a= "))
b = float(input("Enter the value b= "))
c = float(input("Enter the value c= "))
phuong_trinh_1 = float(-b + math.sqrt(b * b - 4 * a * c) / 2 * a)
print(phuong_trinh_1)
#anh chị nào chấm bài này cứu em, sao em bấm quài khong được cũng kh bít sai ở đâu huhuhuhuhu :((((