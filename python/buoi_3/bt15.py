'''
Bài15:Nhậpvàonămsinhcủamộtngườivàtínhtuổicủangườiđó.
Gợi ý:
Cho nhậpvàocácgiátrịsốthựcvàgánvàocácbiến: namSinh
Sửdụngthưviện: from datetime import date  
Đểlấyđượcnămhiệntại:  today = date.today()  
*ý tưởng
b1: viết lời chào
b2: import thư viện datetime
b2.1: gán giá trị cho một biến để lấy được năm hiện tại
b3:lấy năm hiện tại trừ cho năm sinh => tuổi
'''
import datetime
dt = datetime.datetime.now() 
print("\t-------------------CALCULATOR OF AGE-------------------")
nam_hien_tai = float(dt.year)
yob = float(input("Enter your year of birth: "))
print(f"My age: ", nam_hien_tai - yob)

