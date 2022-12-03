'''
Bài 5: Tính tổng các số LẼ nằm trong đoạn từ 0 đến N
Gợi ý:
Khai báo một biến tong_le = 0.
Dùng vòng lặp cho chạy từ i đến N
Kiểm tra điều kiện xem i có thỏa điều kiện không chia hết cho 2 hay không, nếu thỏa điều kiện thì
cộng dồn giá trị của i vào biến tong_le.
Xuất kết quả biến tong_le ra màn hình
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
i = 1
while i < n+1:
    if i % 2 != 0:
        sum = sum + i

    i += 1

print(f"Kết quả: {sum}")