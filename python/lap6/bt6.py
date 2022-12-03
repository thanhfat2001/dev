'''
Bài 6: Tính trung bình cộng các số trong mảng
Gợi ý:
Khai báo một biến tong = 0.
Dùng vòng lặp cho chạy từ i đến N
Cộng dồn giá trị của i vào biến tong
Xuất kết quả trung bình các số là: tong/20 ra màn hình
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

sum  = 0 
count = 0
average = 0
i = 1
while i < n+1:
    sum = sum + 1
    count = count + 1
    i += 1
average = sum/count
print(f"Sum of average: {average}")