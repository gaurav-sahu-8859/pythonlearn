# # list #mutable

# #  0  1 2  3 4
# l=[2,34,5,78,7]
# # l=list([2,34,5,78,7])
# # l.append("apple") # add from last
# l.pop() # remove from last default or pass index number so remove by index
# l[0]=9
# print(l)


# # case1) for i in range(len(l)):
# #             #print(i)#0,1,2,3,4
# # case2) for i in l:
# #             #print(i)#2,34,5,78


# # tuple #immutable
# t=(2,34,5,78,7)
# # t=tuple([2,34,5,78,7])
# # t[0]=9 #error found

# # update way
# dummy=list(t)
# dummy[0]=9
# t=tuple(dummy)


# print(dummy)
# print(t)


# set #mutable
# s={2,34,5,2,3,78,7}
# s=set({2,34,5,2,3,78,7})
s={"apple","banana","orange"}

# frozenset
# s=frozenset(s) #immutable

# s.add("cherry")
print(s)


