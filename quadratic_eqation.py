import math
a=float(input("enter cofficient a:"))
b=float(input("enter cofficient b:"))
c=float(input("enter cofficient c:"))
d=(b**2)-(4*a*c)
print("root1=",(-b-math.sqrt(d))/(2*a))
print("root2=",(-b+math.sqrt(d))/(2*a))

