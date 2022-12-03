'''
Bài 3: Kiểm tra xem tháng có bao nhiêu ngày với dữ liệu:
• Tháng có 31 ngày: 1,3,5,6,8,10,12
 TRƯỜNG ĐẠI HỌC VĂN LANG______________________________Cơ Sở Lập Trình – Khoa Công Nghệ Thông Tin
____________________________________________________________ 2 | Th.S Trần Quang Nhật - Th.S Nguyễn Minh Tân 
• Tháng có 30 ngày: 4,6,9,11
• Tháng 2 thì cần biết năm nhuần thì 29 ngày và 28 ko nhuần

'''
#b1 hien thi loi chao
print("\t-----PROGRAM TO CHECK LEAP YEAR-----")
#b2 nhap thang, nam
month = int(input("Please enter a month in numeric from 1-12: "))
year = input("Please enter a year to be checked: ")
if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    print("Valid month with 31 days")
elif month == 4 or 6 or 9 or 11:
    print("Valid month with 30 days")

else: #month == 2
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")