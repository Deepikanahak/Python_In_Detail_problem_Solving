#8. Find GCD of two numbers
def GCD(a,b):
    if b==0:
        return a 
    return GCD(b,a%b)
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(GCD(a,b))
