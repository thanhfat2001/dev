'''
Bài 7: Tính tổng giá trị từ 1 đến N, nếu chạy đến số 13 thì không chạy nữa và xuất kết quả
Gợi ý: 
Khai báo một biến ketQua = 0. 
Dùng vòng lặp cho chạy từ i đến N
Kiểm tra điều kiện xem i có bằng 13 hay không, nếu i chưa bằng thì cộng dồn giá trị của i vào biến 
ketQua. Ngược lại, i = 13 thì dùng lệnh break để thoát khỏi vòng lặp
Xuất kết quả biến ketQua ra màn hình
'''

n = ''
while True:
    try: 
        n = int(input("Enter number: "))
        if n < 13:
            print("Continue")
        elif n == 13:
            break
    except:
        print("Not valid, try to enter number again: ")

ketqua = 0
for x in range(1,n+1,1):
        ketqua += x

print(f"Sum of N: {ketqua}")