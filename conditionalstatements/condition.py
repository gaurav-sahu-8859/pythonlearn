# # condition statements
# 1) if-else
    #   a) nested if-else
    #   a) if-else ladder
# 2) match


# # if-else syntax
# if(condition1):
#     # code
# elif(condition2):
#     # code
# ................
# else:
#     # code

# age=int(input("enter you age:"))
# if(age>=18):
#     print("can vote")
#     if(age==18 or age==19 ):
#         print("also teenager")
#     elif(age>45):
#         print("age is greater than 45")
#     elif(age==45):
#         print("age is 45")
#     else:
#         print("age is lesser than 45")
# elif(age>12 and age<18):
#     print("teenager")
# elif(age<5):
#     print("just born")
# else:
#     print("you are in range b/w 5-12")


# tasks   ternary
# 1) determine no is odd or even
# 2) determine character is vowel or consonent
# 3) determne no is +ive or -ive
# 4) determine symbol is alphabet or not (isalpha())
# 5) determine symbol is digit or not (isdigit())


# nested if task
# 1)age>=18
# 2)qualification = bca |mba|etc
# 3) experiance > 2




# syntax of match
# match(varname):
#     case v1:
#         # code
#     case v2:
#         # code
#     case _:
#         # code
# balance=500
# print("1) withdraw \n2) check balance\n3) deposit")
# choice=int(input("enter your choice:"))
# # print( "choice is 1" if (choice==1)else"another choice" "choice is 2" if(choice==2) else "another choice")

# match(choice):
#     case 1:
#         amt=int(input("enter amount:"))#4000
#         if(balance>=amt):
#             balance-=amt
#             print("withdraw:",amt,"balance:",balance)
#         else:
#             print("insufficient balance!")
#     case 2:
#         print("balance:",balance)
#     case 3:
#         amt=int(input("enter amount:"))
#         balance+=amt
#         print("balance:",balance)



# # vowel or consonent
# ch=input("enter char:")
# print("vowel" if(ch=="a" or ch=="o" or ch=="i" or ch=="e") else "consonent")