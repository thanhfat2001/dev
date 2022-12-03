'''
Bài 1: Viết chương trình thực hiện các công việc sau :
Nhập 1 số nguyên dương n bất kì (n < 1000).
Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
Tính tổng các chữ số của số đó.
Hiển thị kết qủa ra màn hình
b1: nhap n (n < 1000)
b2: khai bao 1 bien sum de cong don cac gia tri sau moi lan tach hcu so
b3: su dung phep toan module (%) de tach tung chu so
b4: cong gia tri vua tach vai bien sum
b5: su dung phep toan vua chia lay phan nguyen cho 10 de bo 1 chu so vua tach
b6: lap lai buoc 3 va 5 cho toi khi gia tri n = 0 thi dung`
'''
#kiemtra gia tri n < 1000, neu khong hop le thi nhap lai
n = ''
while True:
    try: #doan code nghi ngo loi
        n = int(input("Enter a number: "))
        if n < 0 or n > 1000:
            print("Sorry, please enter N in the format n > 0 && n <1000")
        else: 
            break
    except:
        #khi co loi xay ra thi chay vao day
        print("Not valid, try to enter a numer again. ")

#print(f"You entered: {n}")
sum = 0 
while n > 0:
    digit = n % 10
    sum += digit #sum = sum + digit
    n = n // 10

print(f"Sum of degits: {sum}")
