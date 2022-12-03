#Bài 1: #1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
'''
* Ý tưởng quá trình xử lý:
B1: Hiển thị lời chào
B2: Cho nhập vào:
    +Tên thành phố
    +Tên pet
B3: Hiển thị tên city và pet ra brand name
'''


#b1 hien thi loi chao
print("\t***********************************")
print("\t WELCOME TO THE BAND NAME GENERATOR")
print("\t***********************************")
#b2 nhap ten city pet
city = input("What's the name of the city nyou grew up in ") #nhap ten thanh pho
pet = input("What's your pet's name? ") #nhap vao ten pet
#b3 hien thi loi chao
print ("Your band name: " +city + " " +pet)