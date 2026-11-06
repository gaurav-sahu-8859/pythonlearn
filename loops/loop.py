# # loops
# 1) for 
#     a) for in range(start,end,steps)
#             # code
#     b) for in list
#             # code
# 2) while

# #  0 1 2 3 4 
# l=[3,4,5,7,8]

# for i in l:
#     print(i)

# print("first element of l:",l[0])
# print("lenth of l:",len(l))#5

# for i in range(len(l)):
#     print("i:",i,"->",l[i])
# num=int(input("enter a number:"))

start=5
end=10
for num in range(start,end+1):
    print("table of:",num)
    for i in range(1,10+1):
        print(num,"x",i,"=",num*i)
    print()


# do the same work using user input or using list


# while(condition):
#     #code
i=1
while(i<=10):
    print(i)
    i+=1
