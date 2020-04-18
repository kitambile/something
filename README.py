
x=int(input("enter account number: "))
#   x=385
while (x!= 385):
    print("incorrect number")
    print("try again")
    x=int(input("enter account number: "))
a=int(1000000)
print("Your balance is: " + str(a) + " dollars")

f=input("Do you want to make a deposit or withdrawal: ")

while (f=="deposit"):
    g=int(input("enter amount you want to deposit"))
    balance=("Your total balance after deposit is: "+ str(a+g))
    a=a+g
    print(balance)
    f=(input("Do you want to make a deposit or withdrawal or are you done?"))
    if(f=="done"):
        print("ok bye")


while (f=="withdrawal"):
    e=int(input("enter amount you want to withdraw: "))
    if (e>a):
        print("overdraw")
    balance=("your total balance after withdrawal is " + str(a-e))
    print(balance)
    f=input("do you want to make a deposit or withdrawal or are you done?")
    if (f=="done"):
        print("ok bye!")










