'''
#Bài 2:Tip Calculatorss
#Instructions
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
* ý tưởng - quá trình thực hiện
B1: Hiển thị lời chào cho trương trình
B2: Nhập vào các giá trị
    +tổng tiền cần thanh toán
    + % cần tip
    + số người cần thanh toán
B3: thực hiện tính tiền: tổng (bill + tip) / số người
B4: Hiển thị số tiền mỗi người cần phải trả

'''
#b1: hien thi loi chao
print("\t--------Tip Calculators--------")
#b2: thuc hien tinh toan cho chuong trinh
#b2.1 nhap tong bill thanh toan
bill = float(input("What was the total bill?"))
tip_as_percent = int(input("How much would you like to give?"))
#so tien tip / 100 => so % can tip
people = int(input("How many people to split the bill?"))
#tap 1 bien tip de quy doi tu gia tri %
tip = tip_as_percent / 100 #vi du 12% = ? 12 / 100 = 0.12
total_tip_bill = bill * tip #bill ban dau * tien tip => tong tien phai tra

total_bill = bill + total_tip_bill
# sau khi co dc tong thanh toan (da co tip) thi chia cho so luoong person
bill_per_person = total_bill / people
#su dung templete f-string để hiển thị chuỗi kết hợp với biến
print(f"Each person should pay: ${bill_per_person}")

