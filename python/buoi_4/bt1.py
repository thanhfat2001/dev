'''
Bài 1: Viết chương trình RollerCoaster
Giả sử bạn cần viết chương trình để bán vé cho trò chơi RollerCoaster điều kiện bắt buộc khách 
quan phải cao từ 1m6 (tức là 160 cm) thì mới bán vé:
Giá vé được bán theo hướng dẫn sau:
§ Khách từ 18t: $12
§ Khách từ 16t đến dưới 18t: $7
§ Khách dưới 16t: $5
§ Nếu khách có nhu cầu chụp hình làm kỉ niệm vui lòng phụ thu thêm: $1/ ảnh
'''
#b1 viet loi chao
print("\t*****ROLLERCOASTER*****")
#b2 nhap gia tri
chieu_cao = float(input("Mời bạn nhập chiều cao: "))
tuoi = float(input("Mời bạn nhập tuổi: "))
ncca = float(input("Số lượng ảnh muốn chụp: "))
tien_anh = ncca * 1
tren_18 = 12
tu16_den18 = 7
duoi16 = 5
if chieu_cao >= 160:
    print("Bạn đủ điều kiện để mua vé")
else:
    print("Bạn KHÔNG đủ điều kiện để mua vé")

if tuoi >= 18:
    print("Giá vé là 12$/người")
    print(f"Tổng số tiền thanh toán là: ", (tren_18 + tien_anh), "$")
elif 16 <= tuoi < 18:
    print("Giá vé là 7$/người")
    print(f"Tổng số tiền thanh toán là: ", (tu16_den18 + tien_anh), "$")
elif tuoi < 16:
    print("Giá vé là 5$/người")
    print(f"Tổng số tiền thanh toán là: ", (duoi16 + tien_anh), "$")
        

