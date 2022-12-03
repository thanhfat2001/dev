'''
Bài 3: Tính tổng từ 1 cho đến N
Gợi ý:
Khai báo một biến sum = 0.
Dùng vòng lặp cho chạy từ i đến N rồi cộng dồn giá trị của i vào biến sum
Xuất kết quả biến sum ra màn hình
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
for x in range(1,n+1,1):
        sum += x

print(f"Sum of N: {sum}")