'''
Bài 19: Có một gia đình nọ, gồm 4 người: cha, mẹ và 2 người con. Người cha và người mẹ đều là những người giáo viên gương mẫu nên cách họ dạy con cũng rất đặc biệt. Họ muốn con mình phải hiểu rằng: Muốn có được tiền thì phải tự mình lao động. Vì vậy cả hai người đã lập ra một danh sách các công việc nhà, tương ứng với số tiền con họ sẽ nhận được khi hoàn thành:
Bảng công việc:	
-	Quét nhà: 2.000 đồng
-	Lau nhà: 2.000 đồng
-	Rửa chén 1.000 đồng
-	Ủi quần áo: 1.000 đồng
-	Giặt, phơi quần áo: 2.000 đồng
Người anh cả vì quá mê chiếc balo có hình siêu nhân trị giá 15.000 đồng nên đã rất chăm chỉ. Anh ta làm 4 ngày trong một tuần là 2-4-6-chủ nhật và làm các công việc như sau: quét nhà, rửa chén và ủi quần áo. Còn cô em thì làm 3 ngày trong tuần là 3-5-7 với các công việc như: quét nhà, lau nhà và giặt, phơi quần áo. Hỏi trong một tuần, hai người họ nhận được bao nhiêu tiền từ bố mẹ? Và người anh có đủ tiền để mua chiếc balo không?
*ý tưởng
b1:viết lời chào
b2: nhập các giá trị công việc của nhà
b2.1: tính số tiền làm được trong 1 tuần : số ngày làm việc * tổng số tiền làm được trong 1 ngày
b3: in ra số tiền mà cả 2 làm được
b4:xuất ra màn hình người anh có đủ tiền mua ba lô hay không với lệnh if

'''
print("\t---------------Tính số tiền mà hai anh em kiếm được trong một tuần---------------")
quet_nha = 2000
lau_nha = 2000
rua_chen = 1000
ui_quan_ao = 1000
giat_quan_ao = 2000
cong_viec_cua_anh = (quet_nha + rua_chen + ui_quan_ao)
cong_viec_cua_em = (quet_nha + giat_quan_ao + lau_nha)
tien_anh = (4 * cong_viec_cua_anh)
tien_em = (3 * cong_viec_cua_em)
print("Số tiền mà người anh làm được trong 1 tuần là: ", tien_anh)
print("Số tiền mà người em làm được trong 1 tuần là: ", tien_em)
if tien_anh >= 15000:
    print("Người anh đủ tiền mua balo")
if tien_anh <= 15000:
    print("Người anh không đủ tiền mua balo")
    