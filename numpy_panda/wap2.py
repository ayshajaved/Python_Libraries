# #arithemtic progession
# s = int(input("Enter the starting value:- "))
# d = int(input("Enter the difference:- "))
# e = int(input("Enter the ending value:- "))
# values = []
# for i in range(s, e+1, d):
#     values.append(i)
# print("Printing the arithmetic progression values: ")
# print(values)
# g = []
# term = s
# while term<e:
#     g.append(term)
#     term*=d

# print("Printing the Geometric progression:-")
# print(g)

'''
using list comprehension
'''
s = int(input("Enter the starting value:- "))
d = int(input("Enter the common ratio:- "))
e = int(input("Enter the number of terms:- "))
ap = [s+d*i for i in range(e)]
print(ap)
gp = [s*(d ** i) for i in range(e)]
print(gp)