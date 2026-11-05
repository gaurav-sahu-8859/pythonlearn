# # arithmatic operator(+,-,/,*,%,**,//)
# a=int(input("enter first no:"))#"2"->2 #2725%10
# b=int(input("enter second no: "))#"2"->2
# print("addition:",a+b)
# print("remainder:",5%2)
# print("power:",a**b)
# print("division:",5/2)
# print("floor division:",5 //2)

# # assignment operators(=,+=,-=,/=,*=,%=)
# a=5
# a-=2#a=a+2
# print("value of a is:",a)


# # comparision operators(<,>,<=,>=,!=,==)
# a=5
# b=7
# print(a<=b)
# print(2=="2")



# logical operators(and,or,not)
a=5
b=7
#       t      t
print((a>4) ^ (b>5))


# # and(&)
# a      b        i/o
# 0      0         0
# 1      0         0
# 0      1         0
# 1      1         1

# # or(|)
# a      b        i/o
# 0      0         0
# 1      0         1
# 0      1         1
# 1      1         1

# # Xor(^)
# a      b        i/o
# 0      0         0
# 1      0         1
# 0      1         1
# 1      1         0


# # not
# a      i/o
# 0      1
# 1      0



# bitwise oerators(&,|,~,<<,>>,^)
# bitwise not(~)
# ~x=-x-1 # ~-5=5-1=4
print("bitwise not:",~-5)


# right shift(>>)
# x>>n=x//(2**n) # 5>>1=5//(2**1)=5//2=2

print("right shift:",5>>2)

# left shift(<<)
# x<<n=x*(2**n) # 5<<1=5*(2**1)=5*2=10
print("left shift:",5<<2)
