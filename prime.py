def prime(x):
    if(x < 2):
        return False
    i =2
    while(i*i<=x):
         if(x%i == 0):
            return False
         i += 1
    return True
num= int (input("Enter number:"))
print(prime(num))
    
