#PROJECT 4 
# SIMPLE BASIC ATM MACHINE
cash=50000
print("Please insert your card!")
a=int(input("enter your pin:-"))
print("pin enterd sucessfully!!",a)
b=int(input("Enter amount to withdraw:-"))
if (b<50000):
    print("Thanks! your transaction is succesfull!\n collect your cash & card\n visit again")
elif(b>50000):
    print("Sorry!! not enough cash available!!")
else:
    print("Transaction not sucessful!!!\n try again!!")
print("Thanks for choosing us!!")
# while True:
#     print("Plz insert atm card")