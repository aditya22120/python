a= int (input("enter first no.: "))
b= int (input("enter second no.: "))
print("enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
c= int (input("enter your choice: "))
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
elif(c==4):
    if(b!=0):
        print(a/b)
    else:
        print("error: division by zero is not allowed")
else:
    print("error: invalid choice")


