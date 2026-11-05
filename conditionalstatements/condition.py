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

age=int(input("enter you age:"))
if(age>=18):
    print("can vote")
    if(age==18 or age==19 ):
        print("also teenager")
    elif(age>45):
        print("age is greater than 45")
    elif(age==45):
        print("age is 45")
    else:
        print("age is lesser than 45")
elif(age>12 and age<18):
    print("teenager")
elif(age<5):
    print("just born")
else:
    print("you are in range b/w 5-12")


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


