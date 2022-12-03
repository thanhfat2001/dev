'''
Bài 2: Pizza Order
Youre got a job at Python Pizz. Your first job is to buil an automatic pizza order program.
Based on a users orders, work out their final bill.
§ Small Pizza: $ 15
§ Medium Pizza: $ 20
§ Large Pizza: $ 25
§ Pepperoni for small Pizza: + $ 2
§ Pepperoni for Medium or Large Pizza : + $ 3
§ Extra cheese for any size pizza: + $ 1
Input: 
• size = “L”
• add_pepperoni = “Y”
• extra_cheese = “N”
Output
q Your final bill is: $28
'''
print("\t*****WELCOME TO PYTHON PIZZ*****")
s = 15
m = 20
l = 25
sr = 15
mr = 20
lr = 25
ps = 2
pml = 3
chese = 1
result = 0;
oder =  input("What size for pizza you want s/m/l/all: ") 
pepperoni = input("Do you want Pepperoni for pizza yes/no: ")
extra_chese = input("Do you want extra chese yes/no: ")
if oder == 's':
    print(f"All bill: {s}")
elif pepperoni == 'y':
    print(f"All bill: ", (s + pml))
elif chese == 'y':
    print(f"All bill: ", (s + chese))
elif oder == "all":
    print(f"All bill: ", (s + ps + chese))

if oder == 'm':
    print(f"All bill: {m}")
elif pepperoni == 'y':
    print(f"All bill: ", (m + pml))
elif chese == 'y':
    print(f"All bill: ", (m + chese))
elif oder == "all":
    print(f"All bill: ", (m + pml + chese))


if oder == 'l':
    print(f"All bill: {l}")
elif pepperoni == 'y':
    print(f"All bill: ", (l + pml))
elif chese == 'y':
    print(f"All bill: ", (l + chese))
elif oder == "all":
    print(f"All bill: ", (l + pml + chese))





