balance=500
choice=1
# print( "choice is 1" if (choice==1)else"another choice" "choice is 2" if(choice==2) else "another choice")
print("balance:",balance)
while(choice!=0):
    print("------------------------------------------------------------------\n\n")
    
    print("1) withdraw \n2) check balance\n3) deposit\n0) exit")
    choice=int(input("enter your choice:"))
    match(choice):
        case 1:
            amt=int(input("enter amount:"))#4000
            if(balance>=amt):
                balance-=amt
                print("withdraw:",amt,"balance:",balance)
            else:
                print("insufficient balance!")
        case 2:
            print("balance:",balance)
        case 3:
            amt=int(input("enter amount:"))
            balance+=amt
            print("balance:",balance)

