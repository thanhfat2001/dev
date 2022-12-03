'''
Bài 4: Tính tổng các số CHẴN nằm trong đoạn từ 0 đến N
Gợi ý:
Khai báo một biến tongChan = 0.
Dùng vòng lặp cho chạy từ i đến N
Kiểm tra điều kiện xem i có thỏa điều kiện chia hết cho 2 hay không, nếu thỏa điều kiện thì cộng
dồn giá trị của i vào biến tongChan.
Xuất kết quả biến tongChan ra màn hình
'''
n = ''
while True:
        try:
        #doan code nghi ngo loi
                n = int(input("Enter a number: "))
                if n < 0 or n > 1000:
                        print("Sorry, please enter N in the format n > 0 && n < 1000")
                else:
                        break
        except:
                #Khi co loi xay ra chay vao day
                print("Not valid, try to enter number again: ")

sum = 0 
for i in range(2,n+1,2):
    sum += i

print(f"Sum of N: {sum}")