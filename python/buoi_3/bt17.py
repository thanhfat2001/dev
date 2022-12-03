
'''Bài 17:Nhậpđiểmthivàhệsố 3 mônToán, Lý, Hóacủamộtsinhviên. Tínhđiểmtrungbìnhcủasinhviênđó.
Gợi ý:
Cho nhậpvàocácgiátrịsốthựcvàgánvàocácbiến: diemToan, diemLy, diemHoa.
Côngthức: ĐTB = (diemToan + diemLy + diemHoa) / 3
*ý tưởng
b1: hiển thị lời chào
b2: nhập điểm toán, lý, hóa
b3: tính điểm trung bình
'''
print("\t-------------------CALCULATOR AVERAGE-------------------")
toan = float(input("Nhập điểm toán= "))
ly = float(input("Nhập điểm lý= "))
hoa = float(input("Nhập điểm hóa= "))
average = float((toan + ly + hoa) / 3)
print(f"Điểm trung bình 3 môn toán lý hóa là: ", average)
