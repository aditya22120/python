import random
def ran(a,b):
    return random.randint(a,b)
a = int ( input ("Enter the lower limit:"))
b = int ( input ("Enter the upper limit:"))
print(ran(a,b))