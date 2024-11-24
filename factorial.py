def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

num = int(input("Enter a number: "))
print("Factorial of", num, "is", fact(num))
if(armstrong(153)):
    print("Armstrong number")
else:
    print("Not an armstrong number")
