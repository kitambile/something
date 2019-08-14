
x=int(input("enter account number: "))
# x=385
while(x!= 385):
    print("incorrect number")
    print('try again')
    x=int(input("enter account number: "))
a=int(1000000)
print("Your balance is: " + str(a) + " dollars")
f=input("Do you want to make a deposit or withdfrawal")

while (f=="deposit"):
    g=int(input("enter amount you want to deposit"))
    balance=("Your total balance after deposit is: "+ str(a+g))
    a=a+g
    print(balance)
    f=int(inp)


