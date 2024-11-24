def prime(x):
    for i in range(2, int(x**0.5) + 1):
        if (x % i == 0):
            return False
        return True
a = int(input("Enter start interval:"))
b = int(input("Enter end interval:"))
for i in range(a, b):
    if prime(i):
        print(i)
        