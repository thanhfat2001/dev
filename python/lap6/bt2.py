'''
Bài 2: Viết chương trình thực hiện các công việc sau:
Nhập 3 số a, b, c bất kì
Hãy kiểm tra ba số đó có phải là độ dài của các cạnh của một tam giác hay không?
Nếu đúng là tam giác thì xác định là tam giác vuông hay không?
Ý tưởng:
b1: khai báo và nhập 3 biến để lưu trữ 3 cạnh tam giác a, b, c
b2: nếu canh1 + canh2 > canh3 thì đó là tam giác
'''
canh1 = int(input("Enter side1: "))
canh2 = int(input("Enter side2: "))
canh3 = int(input("Enter side3: "))
if (canh1 + canh2 > canh3) and (canh1 + canh3 > canh2) and (canh2 + canh3 > canh1):
#kiem tra tam giac vuong
    if (canh1*canh1 == canh2*canh2 + canh3*canh3) or  (canh2*canh2 == canh1*canh1 + canh3*canh3) or  (canh3*canh3 == canh1*canh1 + canh2*canh2):
        print("This is a right triangle")
    elif canh1 == canh2 and canh2 == canh3:
        print("This is a triangle equilateral")
    elif canh1 == canh2 or canh1 == canh3 or canh2 == canh3:
        print("This is a triangle isosceles")
    else:
        print("This is a simple triangle")
else:
    print("Not triangle")