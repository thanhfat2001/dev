'''
Bài 16:Nhậpvàotênsảnphẩm, sốlượngvàđơngiá. Tínhtiềnthuếgiátrịgiatăngphảitrả, biếtrằng: 
Tiền = sốlượng * đơngiá
Thuếgiátrịgiatăng = 10% * tiền
*ý tưởng
b1: hiển thị lời chào
b2: nhập tên sản phẩm, số lượng và đơn giá
b3: tính thuế GTGT:

'''
print("\t-------------------Tính thuế GTGT-------------------")
san_pham = input("Nhập tên sản phẩm: ")
so_luong = float(input("Số lượng: "))
don_gia = float(input("Đơn giá của sản phẩm: "))
money = float(so_luong * don_gia)
#máy tính sẽ không nhân được với 10% nên đổi thành / 10 thì sẽ ra kết quả
gtgt = float(money / 10) 
print(f"Thuế giá trị gia tăng của", san_pham, "là: " , gtgt)